"""Scrape geosamples.org material-types, compare against the SESAR materials
extension and mineralSKOS vocabularies, and write a CSV annotated with matches.

Two join keys, checked against each vocabulary in turn:

  API label             <-> skos:prefLabel  (case-insensitive; label casing is
                                             not significant in either source)
  API material_type_uri <-> the concept's "match URI"

A concept's match URI is its own URI for SESAR_materials_extension. For
mineralSKOS the API refers to minerals by mindat URI rather than by the native
gcmin: URI, so the match URI is, in order of preference:

  1. a skos:exactMatch in the https://www.mindat.org namespace
  2. any other declared skos:exactMatch (lowest sorting, for determinism)
  3. the concept's own gcmin: URI

CURIEs on both sides are expanded via the @prefix declarations in the ttl files;
the API returns a mix of full URIs and unexpanded sesrs:/rksd: CURIEs.

Each row also carries skos:definition from the matched concept, and Natalie
Raia's Keep/Remove review decision parsed from REVIEW (a markdown export of the
MaterialType_Vocabulary_Review Google Doc).

Mineral descriptions are normalized to one style:

  strunz:X. Notes: Y. Elements: Z. Crystal system: W. IMA number: N.

replacing the pipe-delimited style the API returns. Values come from MINERALS
(MineralsList.xlsx), matched case-insensitively on the gcmin: local name against
that sheet's 's' column and falling back to its 'label' column, laid over the
fields parsed back out of the original description -- so nothing the sheet lacks
is lost, and rows with no sheet row are still reformatted from their own
content. Empty values drop their whole segment.

Needs openpyxl in addition to rdflib.
"""
import collections
import csv
import json
import re
import urllib.request

import openpyxl
import rdflib
from rdflib.namespace import RDF, SKOS

API = "https://api2.geosamples.org/api/vocab/material-types"
JSON_OUT = "material-types.json"
CSV_OUT = "material-types-skos-comparison.csv"
REVIEW = "MaterialType_Vocabulary_Review.md"
REVIEW_OUT = "material-type-review-vs-skos.csv"
MINERALS = r"C:/GithubC/IEDA/vocabularies/vocabulary/MineralsList.xlsx"
GCMIN_NS = "https://w3id.org/geochem/1.0/min/"
ROCKSED = (r"C:/GithubC/IEDA/vocabularies/vocabulary/"
           r"SESAR_material_extension_rock_sediment bkuttl")
VOCABS = [                       # (name, path, match-URI strategy)
    ("SESAR_materials_extension",
     r"C:/GithubC/IEDA/vocabularies/vocabulary/SESAR_materials_extension.ttl", "self"),
    ("mineralSKOS",
     r"C:/GithubC/IEDA/vocabularies/vocabulary/mineralSKOS.ttl", "exactmatch"),
]
MINDAT = "https://www.mindat.org/"

# --- fetch --------------------------------------------------------------
# JSON_OUT is committed: it is the baseline the edit diff is computed
# against, not a scratch cache. Delete it only to deliberately re-baseline
# against a fresh download, which invalidates sesar-material-type-edits.csv.
try:
    rows = json.load(open(JSON_OUT, encoding="utf-8"))["data"]
except FileNotFoundError:
    with urllib.request.urlopen(API) as r:
        raw = r.read().decode("utf-8")
    open(JSON_OUT, "w", encoding="utf-8").write(raw)
    rows = json.loads(raw)["data"]


def norm(uri):
    """Normalize for comparison: mindat is served from both hosts."""
    if not uri:
        return uri
    return uri.replace("https://mindat.org/", MINDAT, 1)


class Vocab:
    def __init__(self, name, path, strategy):
        self.name = name
        g = rdflib.Graph()
        g.parse(path, format="turtle")
        self.prefixes = {p: str(n) for p, n in g.namespaces()}
        concepts = set(g.subjects(RDF.type, SKOS.Concept))

        self.labels = {str(s): [str(o) for o in g.objects(s, SKOS.prefLabel)]
                       for s in concepts}
        self.definitions = {
            str(s): [str(o).strip() for o in g.objects(s, SKOS.definition)
                     if str(o).strip()]
            for s in concepts}
        self.match_uri = {}
        self.match_uri_source = {}
        for s in concepts:
            u = str(s)
            if strategy == "self":
                self.match_uri[u], self.match_uri_source[u] = u, "concept uri"
                continue
            exact = sorted(str(o) for o in g.objects(s, SKOS.exactMatch))
            mindat = [e for e in exact if e.startswith(MINDAT)]
            if mindat:
                self.match_uri[u] = mindat[0]
                self.match_uri_source[u] = "mindat exactMatch"
            elif exact:
                self.match_uri[u] = exact[0]
                self.match_uri_source[u] = "other exactMatch"
            else:
                self.match_uri[u] = u
                self.match_uri_source[u] = "gcmin uri (no exactMatch)"

        self.by_label = collections.defaultdict(list)
        for u, ls in self.labels.items():
            for l in ls:
                self.by_label[l.strip().lower()].append(u)
        self.by_uri = collections.defaultdict(list)
        for u, m in self.match_uri.items():
            self.by_uri[norm(m)].append(u)
        srcs = collections.Counter(self.match_uri_source.values())
        print(f"loaded {name}: {len(concepts)} concepts; match uri from "
              + ", ".join(f"{v} {k}" for k, v in srcs.most_common()))


vocabs = [Vocab(*v) for v in VOCABS]
prefixes = {}
for v in reversed(vocabs):          # earlier vocabs win on prefix collisions
    prefixes.update(v.prefixes)


# --- Natalie Raia's review ---------------------------------------------------
# Bullet lines look like:
#   - [term](https://.../file.html#anchor) \[Keep - for faceting only\]
#   - Sedimentary breccia \[Add; hasParent:sedimentaryrock\]
# A term recurs wherever it sits in the hierarchy, so decisions are collected
# per term and only reported as disagreeing when they actually differ.
TAG = re.compile(r"\\\[([^\]]*?)\\\]")
LINK = re.compile(r"\[([^\]]+)\]\(([^)]*)\)")


def load_review(path):
    """Return (terms, parents).

    Bullet indentation carries the hierarchy (2/6/10/... spaces), so the parent
    of a bullet is the nearest preceding bullet indented less. A term appears
    once per position it holds, so it can have several parents.
    """
    section = ""
    seen = collections.defaultdict(
        lambda: {"decisions": [], "tags": [], "anchors": []})
    parents = collections.defaultdict(set)
    stack = []
    for raw in open(path, encoding="utf-8"):
        raw = raw.rstrip("\n")
        if raw.startswith("#"):
            section = raw.lstrip("#").strip()
            stack = []
            continue
        m = re.match(r"^( *)- (.*)$", raw)
        if section != "Tab 1" or not m:
            continue
        indent, body = len(m.group(1)), m.group(2).strip()
        tm = TAG.search(body)
        tag = tm.group(1).strip() if tm else ""
        term_part = body[:body.index("\\[")].strip() if "\\[" in body else body
        # Google Docs splits a link mid-word, e.g. [p](url)[hyllonite](url),
        # so keep every link's text and concatenate rather than taking one.
        anchors = [u.rsplit("#", 1)[1] for _, u in LINK.findall(term_part)
                   if "#" in u]
        term = re.sub(r"\[|\]", "",
                      LINK.sub(lambda x: x.group(1), term_part)).strip()
        if not term:
            continue
        key = term.lower()

        while stack and stack[-1][0] >= indent:
            stack.pop()
        if stack:
            parents[key].add(stack[-1][1])
        stack.append((indent, key))

        e = seen[key]
        word = re.split(r"[\s;,\-–.]", tag, 1)[0].strip().rstrip(":") if tag else ""
        if word and word not in e["decisions"]:
            e["decisions"].append(word)
        if tag and tag not in e["tags"]:
            e["tags"].append(tag)
        for a in anchors:
            if a not in e["anchors"]:
                e["anchors"].append(a)
    print(f"loaded review: {len(seen)} distinct terms, "
          f"{sum(1 for v in seen.values() if len(v['decisions']) > 1)} with "
          f"disagreeing decisions, "
          f"{sum(1 for v in parents.values() if len(v) > 1)} with >1 parent")
    return seen, parents


review, review_parents = load_review(REVIEW)


# --- assigning each reviewed term its most specific surviving URI ------------
# The review prunes the vocabulary, so a term that was Removed no longer has a
# concept of its own. Rows using it are remapped onto the nearest ancestor that
# survived, which is the most specific class that still subsumes them.
#
# URIs come from the rock_sediment vocabulary the review links to, resolved by
# the anchor in the link and falling back to prefLabel; terms outside it (the
# top-level material classes) fall back to the materials extension. This
# vocabulary is loaded only to resolve URIs -- adding it to VOCABS would change
# the match columns.
rock_sediment = rdflib.Graph()
rock_sediment.parse(ROCKSED, format="turtle")
rs_by_local, rs_by_label = {}, {}
for s in rock_sediment.subjects(RDF.type, SKOS.Concept):
    rs_by_local.setdefault(str(s).rsplit("/", 1)[-1].lower(), str(s))
    for o in rock_sediment.objects(s, SKOS.prefLabel):
        rs_by_label.setdefault(str(o).strip().lower(), str(s))
print(f"loaded rock_sediment vocabulary: {len(rs_by_local)} concepts")


# Both ttl files declare the prefix sesrs:, but bind it to different
# namespaces -- sesar/material/ in the materials extension, sesar/rocksediment
# /0.1/ in the rock_sediment file -- and 213 of the 221 rock_sediment concepts
# also exist in the materials extension. The materials extension is the one in
# use, so a rock_sediment hit is mapped onto its equivalent there when one
# exists. Local names differ in case (Dolostone vs dolostone), so the mapping
# goes through the local name rather than a prefix swap.
SESAR_RS = "https://w3id.org/sesar/rocksediment/0.1/"
SESAR_MAT = "https://w3id.org/sesar/material/"
mat_local = {}
for _v in vocabs:
    for _u in _v.labels:
        if _u.startswith(SESAR_MAT):
            mat_local[_u[len(SESAR_MAT):].lower()] = _u


def prefer_materials_extension(uri):
    if uri.startswith(SESAR_RS):
        return mat_local.get(uri[len(SESAR_RS):].lower(), uri)
    return uri


def term_uri(term):
    """Resolve a reviewed term to a concept URI, or '' if it has none."""
    entry = review.get(term, {})
    for anchor in entry.get("anchors", []):
        hit = rs_by_local.get(anchor.strip().lower())
        if hit:
            return prefer_materials_extension(hit)
    if term in rs_by_label:
        return prefer_materials_extension(rs_by_label[term])
    for v in vocabs:                       # top-level classes live here instead
        hit = v.by_label.get(term)
        if hit:
            return hit[0]
    return ""


# Decisions that count as "the term survives the review". Modify is included
# because it means renamed-but-retained: the concept survives under a new label,
# so it is still selectable and must not be treated as pruned away. Leaving it
# out made a kept sibling look like the sole survivor of a parent.
SURVIVING = {"Keep", "Modify"}


def is_kept(term):
    return bool(SURVIVING & set(review.get(term, {}).get("decisions", [])))


review_children = collections.defaultdict(set)
for _child, _ps in review_parents.items():
    for _p in _ps:
        review_children[_p].add(_child)

_survivor_cache = {}


def subtree(node, _seen=frozenset()):
    """Every term under node, node included."""
    if node in _seen:
        return set()
    seen = _seen | {node}
    out = {node}
    for child in review_children.get(node, ()):
        out |= subtree(child, seen)
    return out


def survivors(node):
    """Kept terms under node, node itself included."""
    if node not in _survivor_cache:
        _survivor_cache[node] = {t for t in subtree(node) if is_kept(t)}
    return _survivor_cache[node]


def absorbing(term):
    """Climb while `term` is the only survivor in the ancestor's subtree.

    Pruning leaves a kept term standing in for everything removed around it. A
    user holding a quartz anorthosite now has to register it as 'anorthosite',
    so SESAR's 'anorthosite' covers what 'anorthositic rock' used to cover and
    has to map to that broader URI. Climbing stops as soon as an ancestor still
    holds another survivor, because then its coverage is split between them
    rather than absorbed by this one.
    """
    current = {term}
    while True:
        higher = {p for a in current for p in review_parents.get(a, set())
                  if survivors(p) == {term}}
        if not higher:
            return sorted(current)
        current = higher


def subsuming_uris(term):
    """(uris, source_terms, absorbed_terms) for a reviewed term."""
    if is_kept(term):
        targets = absorbing(term)
        absorbed = set()
        for t in targets:
            absorbed |= {x for x in subtree(t) if not is_kept(x)}
        return ([term_uri(t) for t in targets], targets,
                sorted(absorbed - {term}))
    # A removed term is registered under whichever surviving term absorbed it,
    # so it resolves to whatever that survivor resolves to -- 'quartz
    # anorthosite' follows 'anorthosite' to the anorthositic rock URI. The
    # survivor need not be an ancestor: look for the nearest level whose subtree
    # still holds one, starting with the term's own.
    seen_terms = set()
    frontier = {term}
    while frontier:
        choices = sorted({s for f in frontier for s in survivors(f)})
        if choices:
            uris, srcs = [], []
            for c in choices:
                u, s, _ = subsuming_uris(c)
                uris += u
                srcs += s
            return list(dict.fromkeys(uris)), list(dict.fromkeys(srcs)), []
        seen_terms |= frontier
        nxt = set()
        for t in frontier:
            nxt |= review_parents.get(t, set()) - seen_terms
        frontier = nxt
    return [], [], []


def expand(value):
    if not value:
        return None, False
    v = value.strip()
    if "://" in v:
        return v, True
    prefix, sep, local = v.partition(":")
    if sep and prefix in prefixes:
        return prefixes[prefix] + local, True
    return v, False


FIELDS = ["id", "label", "alt_label", "description", "material_type_uri",
          "parent_material_types", "source", "scheme_uri", "for_registration",
          "suppress_from_search"]
EXTRA = ["skos_match_status", "skos_match_method", "skos_vocabulary",
         "skos_concept_uri", "skos_match_uri", "skos_preflabel",
         "skos_definition", "review_decision", "review_reason",
         "assigned_material_type_uri", "assigned_uri_from",
         "skos_match_detail", "material_type_uri_expanded"]

counts = collections.Counter()
methods = collections.Counter()
vcounts = collections.Counter()
rcounts = collections.Counter()
defgap = 0
out = []
for r in rows:
    label = (r.get("label") or "").strip()
    api_uri = r.get("material_type_uri")
    expanded, resolvable = expand(api_uri)
    nexp = norm(expanded)

    hit = None
    for v in vocabs:                       # first vocabulary to match wins
        L = v.by_label.get(label.lower(), [])
        U = v.by_uri.get(nexp, []) if nexp else []
        if L or U:
            hit = (v, L, U)
            break

    detail = []
    if api_uri and not resolvable:
        detail.append("api uri is an unresolvable CURIE")

    if hit is None:
        status, method, vocab = "no match", "none", None
        concept = muri = ""
        pref = []
    else:
        v, L, U = hit
        vocab = v.name
        if expanded and nexp != expanded and U:
            detail.append("matched after normalizing mindat host")
        if len(L) > 1:
            detail.append(f"label ambiguous: {len(L)} concepts")
        if L and U:
            shared = sorted(set(L) & set(U))
            if shared:
                concept = shared[0]
                status, method = "match", "label+uri"
            else:
                concept = L[0]
                status = "conflict: label and uri point to different concepts"
                method = "label+uri"
                detail.append(f"api uri resolves to {U[0]} "
                              f"(prefLabel {'; '.join(v.labels[U[0]])})")
        elif L:
            concept = L[0]
            method = "label"
            if expanded:
                status = "label match; api uri not in skos"
                cmp_uri = norm(v.match_uri[concept])
                if cmp_uri.rsplit("/", 1)[0] == nexp.rsplit("/", 1)[0]:
                    detail.append("same namespace, local name differs")
                else:
                    detail.append(f"namespace differs: api {nexp.rsplit('/', 1)[0]}/ "
                                  f"vs skos {cmp_uri.rsplit('/', 1)[0]}/")
            else:
                status = "label match; no uri in api record"
        else:
            concept = U[0]
            status = "uri match; label differs from prefLabel"
            method = "uri"
            detail.append(f"skos prefLabel is {'; '.join(v.labels[concept])}")
        pref = v.labels[concept]
        muri = v.match_uri[concept]
        if v.match_uri_source[concept] != "concept uri":
            detail.append(f"skos match uri from {v.match_uri_source[concept]}")

    definition = ""
    if hit is not None:
        definition = " | ".join(hit[0].definitions.get(concept, []))
    if definition and not (r.get("description") or "").strip():
        defgap += 1

    # Review terms are matched on the API label, falling back to the matched
    # concept's prefLabel for the few the reviewer named by prefLabel instead.
    rterm = label.lower() if label.lower() in review else ""
    if not rterm:
        for p in pref:
            if p.strip().lower() in review:
                rterm = p.strip().lower()
                break
    entry = review.get(rterm) if rterm else None
    decision = "|".join(entry["decisions"]) if entry else ""
    reason = " | ".join(entry["tags"]) if entry else ""
    uris, srcs, absorbed = subsuming_uris(rterm) if rterm else ([], [], [])
    assigned = "|".join(u for u in uris if u)
    assigned_from = "|".join(srcs) if srcs != [rterm] else ""
    rcounts[decision or "(not reviewed)"] += 1

    counts[status] += 1
    methods[method] += 1
    vcounts[vocab or "(none)"] += 1
    out.append({
        **{k: r.get(k) for k in FIELDS},
        "parent_material_types": "|".join(r.get("parent_material_types") or []),
        "skos_match_status": status,
        "skos_match_method": method,
        "skos_vocabulary": vocab or "",
        "skos_concept_uri": concept,
        "skos_match_uri": muri if muri != concept else "",
        "skos_preflabel": "|".join(pref),
        "skos_definition": definition,
        "review_decision": decision,
        "review_reason": reason,
        "assigned_material_type_uri": assigned,
        "assigned_uri_from": assigned_from,
        "skos_match_detail": "; ".join(detail),
        "material_type_uri_expanded": expanded if (api_uri and expanded != api_uri) else "",
    })

# --- append mineral detail from MineralsList.xlsx ----------------------------
def load_minerals(path):
    """Index the sheet by lowercased 's' local name and by lowercased label."""
    ws = openpyxl.load_workbook(path, read_only=True, data_only=True)["MineralsList"]
    it = ws.iter_rows(values_only=True)
    hdr = [str(h).strip() for h in next(it)]
    by_s, by_label = {}, {}
    n = 0
    for raw in it:
        rec = dict(zip(hdr, raw))
        n += 1
        if rec.get("s"):
            by_s.setdefault(str(rec["s"]).split(":", 1)[-1].strip().lower(), rec)
        if rec.get("label"):
            by_label.setdefault(str(rec["label"]).strip().lower(), rec)
    print(f"loaded minerals sheet: {n} rows, {len(by_s)} distinct 's' locals, "
          f"{len(by_label)} distinct labels")
    return by_s, by_label


# Prefix per column, following the requested
#   'strunz:'&[strunz] & '. Notes: '&[notes] & '. Elements: '&[elements]
#     & '. Crystal system: '&[crystal]
# An empty cell drops its whole segment rather than emitting a bare label.
#
# IMA number is not in that format string but IS one of the five fields the
# original pipe-delimited descriptions carry (in 1728 of them), so it is kept
# here -- replacing without it would silently drop data. Drop the last entry to
# match the requested format exactly.
SUFFIX_COLS = [("strunz:", "strunz"), ("Notes: ", "notes"),
               ("Elements: ", "elements"), ("Crystal system: ", "crystal"),
               ("IMA number: ", "ima")]


def mineral_suffix(rec):
    parts = []
    for prefix, col in SUFFIX_COLS:
        val = rec.get(col)
        val = str(val).strip() if val is not None else ""
        if val:
            parts.append(prefix + val)
    return ". ".join(parts) + "." if parts else ""


# The original descriptions state the same facts in a pipe-delimited style,
#   status notes: X| strunz code: Y| elements: Z| Crystal system: W| IMA number: N
# so they are parsed back into fields and the sheet values laid over them. That
# keeps anything the sheet is missing (a couple of minerals have no strunz cell
# but do have a strunz code in the description) and lets rows with no sheet row
# at all still be reformatted from their own content.
PIPE_KEYS = {"status notes": "notes", "strunz code": "strunz",
             "elements": "elements", "crystal system": "crystal",
             "ima number": "ima"}


def parse_pipe(desc):
    fields = {}
    for seg in (desc or "").split("|"):
        label, sep, value = seg.partition(":")
        key = PIPE_KEYS.get(label.strip().lower())
        if sep and key and value.strip():
            fields[key] = value.strip()
    return fields


by_s, by_label = load_minerals(MINERALS)
normalized = nomatch = fromdesc = 0
for row in out:
    uri = row["skos_concept_uri"]
    rec = None
    if uri.startswith(GCMIN_NS):
        local = uri[len(GCMIN_NS):].strip().lower()
        rec = by_s.get(local) or by_label.get(local)
        if rec is None:
            nomatch += 1
    fields = parse_pipe(row.get("description"))
    if rec is not None:                      # sheet wins where it has a value
        for _, col in SUFFIX_COLS:
            val = rec.get(col)
            val = str(val).strip() if val is not None else ""
            if val:
                fields[col] = val
    elif not fields:
        continue
    if rec is None:
        fromdesc += 1
    detail = mineral_suffix(fields)
    if detail:
        row["description"] = detail
        normalized += 1

print(f"mineral descriptions normalized: {normalized} "
      f"({fromdesc} reformatted from their own description, no sheet row); "
      f"{nomatch} gcmin rows had no sheet row")

with open(CSV_OUT, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS + EXTRA)
    w.writeheader()
    w.writerows(out)

# --- review-side output ------------------------------------------------------
# The API no longer carries the terms marked Remove, so those decisions cannot
# appear as a column on an API row. This second file is one row per reviewed
# term, saying where that term still exists.
api_labels = {(r.get("label") or "").strip().lower() for r in rows}
with open(REVIEW_OUT, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["review_term", "review_decision", "review_reason",
                "in_api_material_types"]
               + [f"in_{v.name}" for v in vocabs]
               + ["skos_concept_uri", "own_uri", "assigned_material_type_uri",
                  "assigned_uri_from", "absorbs", "parents"])
    noassign = []
    for term in sorted(review):
        e = review[term]
        hits = [v.by_label.get(term, []) for v in vocabs]
        first = next((h[0] for h in hits if h), "")
        uris, srcs, absorbed = subsuming_uris(term)
        assigned = "|".join(u for u in uris if u)
        if not assigned:
            noassign.append(term)
        w.writerow([term, "|".join(e["decisions"]), " | ".join(e["tags"]),
                    "yes" if term in api_labels else "no"]
                   + ["yes" if h else "no" for h in hits]
                   + [first, term_uri(term), assigned,
                      "|".join(srcs) if srcs != [term] else "",
                      "|".join(absorbed),
                      "|".join(sorted(review_parents.get(term, set())))])
    print(f"\nassigned a subsuming uri to {len(review)-len(noassign)} of "
          f"{len(review)} reviewed terms")
    if noassign:
        print(f"  no surviving ancestor resolved for {len(noassign)}: "
              f"{sorted(noassign)}")

print(f"\napi records: {len(rows)}\nwrote {CSV_OUT} and {REVIEW_OUT}\n")
for k, v in counts.most_common():
    print(f"  {v:5d}  {k}")
print()
for k, v in methods.most_common():
    print(f"  {v:5d}  method={k}")
print()
for k, v in vcounts.most_common():
    print(f"  {v:5d}  vocabulary={k}")
print()
for k, v in rcounts.most_common():
    print(f"  {v:5d}  review={k}")
print(f"\nrows carrying a skos:definition: "
      f"{sum(1 for r in out if r['skos_definition'])}")
print(f"  of which the api description is empty: {defgap}")
unused = sorted(k for k in review
                if not any((r["label"] or "").strip().lower() == k
                           or k in {p.strip().lower()
                                    for p in (r["skos_preflabel"] or "").split("|")}
                           for r in out))
print(f"review terms that join to no api record: {len(unused)} "
      f"({sum(1 for k in unused if review[k]['decisions'] == ['Add'])} of them 'Add')")
