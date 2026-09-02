"""Scrape geosamples.org material-types, compare against the SESAR materials
extension SKOS vocabulary, and write a CSV annotated with match results.

  API label            <-> skos:prefLabel   (case-insensitive)
  API material_type_uri <-> concept URI (CURIEs on both sides expanded via the
                            @prefix declarations in the ttl)
"""
import collections, csv, json, sys, urllib.request
import rdflib
from rdflib.namespace import SKOS, RDF

API = "https://api2.geosamples.org/api/vocab/material-types"
TTL = r"C:/GithubC/IEDA/vocabularies/vocabulary/SESAR_materials_extension.ttl"
JSON_OUT = "material-types.json"
CSV_OUT = "material-types-skos-comparison.csv"

# --- fetch (cached to JSON_OUT so reruns don't re-hit the API) --------------
try:
    rows = json.load(open(JSON_OUT, encoding="utf-8"))["data"]
except FileNotFoundError:
    with urllib.request.urlopen(API) as r:
        raw = r.read().decode("utf-8")
    open(JSON_OUT, "w", encoding="utf-8").write(raw)
    rows = json.loads(raw)["data"]

# --- load the SKOS vocabulary ----------------------------------------------
g = rdflib.Graph()
g.parse(TTL, format="turtle")
prefixes = {p: str(n) for p, n in g.namespaces()}

concepts = set(g.subjects(RDF.type, SKOS.Concept))
uri2labels = {str(s): [str(o) for o in g.objects(s, SKOS.prefLabel)] for s in concepts}
label2uris = collections.defaultdict(list)   # case-insensitive index
for u, labels in uri2labels.items():
    for l in labels:
        label2uris[l.strip().lower()].append(u)

def expand(value):
    """Expand a CURIE against the ttl's prefixes; pass full URIs through."""
    if not value:
        return None, False
    v = value.strip()
    if "://" in v:
        return v, True
    prefix, sep, local = v.partition(":")
    if sep and prefix in prefixes:
        return prefixes[prefix] + local, True
    return v, False

# --- compare ----------------------------------------------------------------
FIELDS = ["id", "label", "alt_label", "description", "material_type_uri",
          "parent_material_types", "source", "scheme_uri", "for_registration",
          "suppress_from_search"]
EXTRA = ["skos_match_status", "skos_match_method", "skos_concept_uri",
         "skos_preflabel", "skos_match_detail", "material_type_uri_expanded"]

counts = collections.Counter()
out = []
for r in rows:
    label = (r.get("label") or "").strip()
    api_uri = r.get("material_type_uri")
    expanded, resolvable = expand(api_uri)

    hits = label2uris.get(label.lower(), [])
    label_uri = hits[0] if hits else None
    uri_hit = expanded in uri2labels if expanded else False

    # Label casing is not significant, so a case-only difference is not
    # reported; URI local names ARE case-sensitive and still are.
    detail = []
    if len(hits) > 1:
        detail.append(f"label ambiguous: {len(hits)} concepts")
    if api_uri and not resolvable:
        detail.append("api uri is an unresolvable CURIE")

    if hits and uri_hit:
        if expanded in hits:
            status, method = "match", "label+uri"
            concept, pref = expanded, uri2labels[expanded]
        else:
            status, method = "conflict: label and uri point to different concepts", "label+uri"
            concept, pref = label_uri, uri2labels[label_uri]
            detail.append(f"api uri resolves to {expanded} (prefLabel "
                          f"{'; '.join(uri2labels[expanded])})")
    elif hits and expanded:
        status, method = "label match; api uri not in skos", "label"
        concept, pref = label_uri, uri2labels[label_uri]
        if expanded.rsplit("/", 1)[0] == concept.rsplit("/", 1)[0]:
            detail.append("same namespace, local name differs")
        else:
            detail.append(f"namespace differs: api {expanded.rsplit('/', 1)[0]}/ "
                          f"vs skos {concept.rsplit('/', 1)[0]}/")
    elif hits:
        status, method = "label match; no uri in api record", "label"
        concept, pref = label_uri, uri2labels[label_uri]
    elif uri_hit:
        status, method = "uri match; label differs from prefLabel", "uri"
        concept, pref = expanded, uri2labels[expanded]
        detail.append(f"skos prefLabel is {'; '.join(pref)}")
    else:
        status, method = "no match", "none"
        concept, pref = None, []

    counts[status] += 1
    parents = r.get("parent_material_types") or []
    out.append({
        **{k: r.get(k) for k in FIELDS},
        "parent_material_types": "|".join(parents),
        "skos_match_status": status,
        "skos_match_method": method,
        "skos_concept_uri": concept or "",
        "skos_preflabel": "|".join(pref),
        "skos_match_detail": "; ".join(detail),
        "material_type_uri_expanded": expanded if (api_uri and expanded != api_uri) else "",
    })

with open(CSV_OUT, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS + EXTRA)
    w.writeheader()
    w.writerows(out)

print(f"api records: {len(rows)}   skos concepts: {len(concepts)}")
print(f"wrote {CSV_OUT}\n")
for k, v in counts.most_common():
    print(f"  {v:5d}  {k}")
print()
import collections as _c
for k, v in _c.Counter(r["skos_match_method"] for r in out).most_common():
    print(f"  {v:5d}  method={k}")
matched = {r["skos_concept_uri"] for r in out if r["skos_concept_uri"]}
print(f"\nskos concepts referenced by at least one api record: {len(matched)} of {len(concepts)}")
print(f"skos concepts never referenced: {len(concepts) - len(matched)}")
