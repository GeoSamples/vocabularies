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
MINDAT = "https://www.mindat.org/"
CONTEXT = ["scheme_uri", "for_registration", "suppress_from_search"]
PAIRED = ["material_type_uri", "parent_material_types", "source", "alt_label",
          "description"]


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
#
# Parent edits live only in the review table, whose `parents` column holds
# review-term names rather than API labels; neither API-shaped file touched
# parent_material_types. Compared as case-insensitive sets, since term casing is
# not significant and the two sources capitalize differently.
review = {(r["review_term"] or "").strip().lower(): r for r in csv.DictReader(
    open(BASE + "material-type-review-vs-skos.csv", encoding="utf-8-sig"))}


def pset(v):
    return {i.strip().lower() for i in (v or "").split("|") if i.strip()}

CHANGE_COLS = ["material_type_uri", "source", "alt_label", "description",
               "label", "scheme_uri"]

rows_out = []
sense_clashes = []
tally = {c: 0 for c in CHANGE_COLS + ["parent_material_types"]}
reformatted = 0
for rid, edited in primary.items():
    base = api[rid]
    rev = review.get((base.get("label") or "").strip().lower(), {})
    # Label joins can cross senses. The review covers rock/sediment classes, so
    # a review term must not lend its parents to a mineral record that merely
    # shares its label -- "dolomite" is the rock in the review (own_uri
    # Dolostone) and the mineral in the API (a mindat URI, parented under
    # Carbonate or Nitrate). Transferring there would reclassify the mineral as
    # a sedimentary rock.
    if (rev and (base.get("material_type_uri") or "").startswith(MINDAT)
            and not (rev.get("own_uri") or "").startswith(MINDAT)):
        sense_clashes.append((rid, base.get("label"), rev.get("own_uri")))
        rev = {}
    proposed_parents = ""
    changed = []
    if rev and pset(rev.get("parents")) != pset(base.get("parent_material_types")):
        proposed_parents = rev.get("parents", "")
        changed.append("parent_material_types")
        tally["parent_material_types"] += 1
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
    for c in PAIRED:
        row[f"{c}_original"] = norm(base.get(c), c)
        if c == "parent_material_types":
            row[f"{c}_updated"] = proposed_parents
        else:
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
          + [f"{c}_{k}" for c in PAIRED for k in ("original", "updated")]
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
if sense_clashes:
    print()
    print("label joins refused as a sense clash "
          "(rock term vs mineral record):")
    for rid, lab, own in sense_clashes:
        print(f"  id={rid} api {lab!r} is a mineral; review term maps to {own}")
print(f"rows flagged as unresolved between the two files: "
      f"{sum(1 for r in rows_out if r['unresolved_disagreement'])}")
print(f"wrote {OUT}")
