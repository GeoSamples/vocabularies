# Why some material types map to a broader URI than their name suggests

Natalie Raia's review of the SESAR material type vocabulary
([google doc](https://docs.google.com/document/d/1p1XlhvBFaulqRWJPdzE2T0rBWc4m6wyUmBAXQi1PC5s/edit))
marks each term Keep, Remove, Modify or Add. Removing a term does not only
delete a row. It changes what the surviving terms around it mean in practice,
and that is what these `material_type_uri` assignments account for.

## The reasoning

When a term is removed, anyone who would have chosen it has to pick the nearest
surviving term instead. That surviving term therefore has to cover everything
the removed terms covered, so its URI has to denote the broader class, not the
narrower concept its label names.

Take **anorthosite**. The review keeps `anorthosite` but removes both its
siblings, `quartz anorthosite` and `foid bearing anorthosite`, and their parent
`anorthositic rock`. Someone registering a quartz anorthosite now has only
"Anorthosite" available. So SESAR's "Anorthosite" no longer means anorthosite
*sensu stricto* — it means what `anorthositic rock` used to mean, and is mapped
to that concept:

    https://w3id.org/isample/earthenv/rocksediment/1.0/Anorthositic_Rock

**Diorite** is the same case: `quartz diorite` and `foid bearing diorite`
removed, `dioritic rock` removed, so "Diorite" maps to
`https://w3id.org/sesar/material/Dioritic_Rock`.

## Where the climb stops

A term moves up only while it is the *only* surviving term beneath the class
above it. As soon as an ancestor still holds another survivor, the climb stops,
because that ancestor's coverage is then divided among several terms rather than
absorbed by one. Anorthosite does not climb past `phaneritic igneous rock`,
which keeps aplite, gabbro, diorite and others.

A term whose parent and siblings all survive keeps its own URI, and that is the
normal case: of 228 surviving terms, only 15 take a broader URI. Terms marked
Modify count as surviving — they are renamed, not deleted.

## The terms affected

Most are QAPF triples, where "foid bearing X" and "quartz X" are removed and "X"
is kept:

| term kept | mapped to |
|---|---|
| anorthosite | anorthositic rock |
| diorite | dioritic rock |
| gabbro | gabbroic rock |
| latite | latitic rock |
| monzodiorite | monzodioritic rock |
| monzogabbro | monzogabbroic rock |
| monzonite | monzonitic rock |
| syenite | syenitic rock |
| trachyte | trachytic rock |
| foidite | foiditoid |
| phonolite | phonolitoid |
| rhyolite | rhyolitoid |
| conglomerate | generic conglomerate |
| dolomite | dolomitic or magnesian sedimentary rock |
| glassy igneous rock | glass rich igneous rock |

## Removed terms

A removed term is given the same URI as the surviving term that absorbed it, so
each family stays internally consistent. `quartz anorthosite`, `foid bearing
anorthosite` and `anorthositic rock` all resolve to `Anorthositic_Rock`
alongside `anorthosite`.

## Scope

73 of the 228 surviving terms absorb at least one removed term. Only the 15
above end up with a broader URI; the others absorb terms narrower than
themselves and so keep their own.

URIs are drawn from the SESAR material vocabulary
(`https://w3id.org/sesar/material/materialvocabulary`), falling back to the
iSamples earth environment rock/sediment vocabulary for classes defined there.
