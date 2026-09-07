"""Build a diff table of hand edits to the SESAR material type records.

Baseline is material-types.json, the original API download. Reports one row per
record whose API-native fields were edited, showing the original value and the
edited value side by side.

Two things are deliberately not treated as edits:

  boolean case      the edited files came back from Excel with TRUE/FALSE where
                    the API has true/false; compared case-insensitively
  mineral descriptions
                    compare_materials.py rewrote 3445 mineral descriptions into
                    one style, so a description only counts as an edit when it
                    also differs from that generated output

sesar-material-types-updates.csv is the primary source. Where
material-types-skos-comparison-smrMatching.csv disagrees, the row is flagged
rather than silently resolved.
"""
import csv
import json

BASE = r"C:/GithubC/IEDA/vocabularies/comparisons/"
OUT = BASE + "sesar-material-type-edits.csv"
EDITABLE = ["label", "alt_label", "description", "material_type_uri",
            "parent_material_types", "source", "scheme_uri",
            "for_registration", "suppress_from_search"]
BOOLS = {"for_registration", "suppress_from_search"}
CONTEXT = ["parent_material_types", "scheme_uri", "for_registration",
           "suppress_from_search"]


def norm(v, col=None):
    if v is None:
        return ""
    if isinstance(v, bool):
        v = "true" if v else "false"
    v = str(v).strip()
    return v.lower() if col in BOOLS else v


api = {}
for r in json.load(open(BASE + "material-types.json", encoding="utf-8"))["data"]:
    rec = dict(r)
    rec["parent_material_types"] = "|".join(r.get("parent_material_types") or [])
    api[str(r["id"])] = rec

generated = {r["id"]: r for r in csv.DictReader(
    open(BASE + "material-types-skos-comparison.csv", encoding="utf-8-sig"))}
primary = {r["id"]: r for r in csv.DictReader(
    open(BASE + "sesar-material-types-updates.csv", encoding="utf-8-sig"))}
alt = {r["id"]: r for r in csv.DictReader(
    open(BASE + "material-types-skos-comparison-smrMatching.csv",
         encoding="utf-8-sig"))}
# The blanked URIs line up with terms the review table reassigns to a broader
# absorbing class, so surface that assignment next to the disagreement.
review = {(r["review_term"] or "").strip().lower(): r for r in csv.DictReader(
    open(BASE + "material-type-review-vs-skos.csv", encoding="utf-8-sig"))}

CHANGE_COLS = ["material_type_uri", "source", "alt_label", "description",
               "label", "parent_material_types", "scheme_uri"]

rows_out = []
tally = {c: 0 for c in CHANGE_COLS}
reformatted = 0
for rid, edited in primary.items():
    base = api[rid]
    changed = []
    for c in CHANGE_COLS:
        if c not in edited:
            continue
        new, old = norm(edited.get(c), c), norm(base.get(c), c)
        if new == old:
            continue
        if c == "description":
            # only an edit if it also differs from the generated normalization
            if new == norm(generated.get(rid, {}).get("description")):
                reformatted += 1
                continue
        changed.append(c)
        tally[c] += 1
    if not changed:
        continue

    other = alt.get(rid, {})
    disagree = [c for c in CHANGE_COLS
                if c in other and norm(other.get(c), c) != norm(edited.get(c), c)]
    row = {"id": rid, "label": base.get("label"),
           "changed_fields": "|".join(changed)}
    for c in ["material_type_uri", "source", "alt_label", "description"]:
        row[f"{c}_original"] = norm(base.get(c), c)
        row[f"{c}_updated"] = norm(edited.get(c), c) if c in changed else ""
    for c in CONTEXT:
        row[f"{c}_original"] = norm(base.get(c), c)
    row["unresolved_disagreement"] = "|".join(disagree)
    row["smrMatching_value"] = "|".join(
        norm(other.get(c), c) or "(blank)" for c in disagree)
    rv = review.get((base.get("label") or "").strip().lower(), {})
    row["review_table_assigns"] = (rv.get("assigned_material_type_uri", "")
                                   if disagree else "")
    rows_out.append(row)

fields = (["id", "label", "changed_fields"]
          + [f"{c}_{k}" for c in ["material_type_uri", "source", "alt_label",
                                  "description"] for k in ("original", "updated")]
          + [f"{c}_original" for c in CONTEXT]
          + ["unresolved_disagreement", "smrMatching_value",
             "review_table_assigns"])
rows_out.sort(key=lambda r: (r["changed_fields"], r["label"] or ""))
with open(OUT, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows_out)

print(f"edited records: {len(rows_out)} of {len(api)}")
for c, n in tally.items():
    if n:
        print(f"  {c:24} {n}")
print(f"\ndescriptions treated as reformatting, not edits: {reformatted}")
print(f"rows flagged as unresolved between the two files: "
      f"{sum(1 for r in rows_out if r['unresolved_disagreement'])}")
print(f"wrote {OUT}")
