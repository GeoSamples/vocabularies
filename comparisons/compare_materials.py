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
VOCABS = [                       # (name, path, match-URI strategy)
    ("SESAR_materials_extension",
     r"C:/GithubC/IEDA/vocabularies/vocabulary/SESAR_materials_extension.ttl", "self"),
    ("mineralSKOS",
     r"C:/GithubC/IEDA/vocabularies/vocabulary/mineralSKOS.ttl", "exactmatch"),
]
MINDAT = "https://www.mindat.org/"

# --- fetch (cached to JSON_OUT so reruns do not re-hit the API) -------------
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
    section = ""
    seen = collections.defaultdict(lambda: {"decisions": [], "tags": []})
    for raw in open(path, encoding="utf-8"):
        if raw.startswith("#"):
            section = raw.lstrip("#").strip()
            continue
        line = raw.strip()
        if section != "Tab 1" or not line.startswith("-"):
            continue
        m = TAG.search(line)
        if not m:
            continue
        body = line[1:].strip()
        tag = m.group(1).strip()
        term_part = body[:body.index("\\[")].strip() if "\\[" in body else body
        # Google Docs splits a link mid-word, e.g. [p](url)[hyllonite](url),
        # so keep every link's text and concatenate rather than taking one.
        term = re.sub(r"\[|\]", "", LINK.sub(lambda m: m.group(1), term_part)).strip()
        if not term:
            continue
        word = re.split(r"[\s;,\-–.]", tag, 1)[0].strip().rstrip(":")
        e = seen[term.lower()]
        if word not in e["decisions"]:
            e["decisions"].append(word)
        if tag not in e["tags"]:
            e["tags"].append(tag)
    print(f"loaded review: {len(seen)} distinct terms, "
          f"{sum(1 for v in seen.values() if len(v['decisions']) > 1)} with "
          f"disagreeing decisions")
    return seen


review = load_review(REVIEW)


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
    entry = review.get(label.lower())
    if entry is None:
        for p in pref:
            entry = review.get(p.strip().lower())
            if entry:
                break
    decision = "|".join(entry["decisions"]) if entry else ""
    reason = " | ".join(entry["tags"]) if entry else ""
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
               + [f"in_{v.name}" for v in vocabs] + ["skos_concept_uri"])
    for term in sorted(review):
        e = review[term]
        hits = [v.by_label.get(term, []) for v in vocabs]
        first = next((h[0] for h in hits if h), "")
        w.writerow([term, "|".join(e["decisions"]), " | ".join(e["tags"]),
                    "yes" if term in api_labels else "no"]
                   + ["yes" if h else "no" for h in hits] + [first])

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
