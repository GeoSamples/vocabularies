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
"""
import collections
import csv
import json
import urllib.request

import rdflib
from rdflib.namespace import RDF, SKOS

API = "https://api2.geosamples.org/api/vocab/material-types"
JSON_OUT = "material-types.json"
CSV_OUT = "material-types-skos-comparison.csv"
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
         "skos_match_detail", "material_type_uri_expanded"]

counts = collections.Counter()
methods = collections.Counter()
vcounts = collections.Counter()
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
        "skos_match_detail": "; ".join(detail),
        "material_type_uri_expanded": expanded if (api_uri and expanded != api_uri) else "",
    })

with open(CSV_OUT, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS + EXTRA)
    w.writeheader()
    w.writerows(out)

print(f"\napi records: {len(rows)}\nwrote {CSV_OUT}\n")
for k, v in counts.most_common():
    print(f"  {v:5d}  {k}")
print()
for k, v in methods.most_common():
    print(f"  {v:5d}  method={k}")
print()
for k, v in vcounts.most_common():
    print(f"  {v:5d}  vocabulary={k}")
