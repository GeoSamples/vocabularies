# Vocabularies folder

## SESAR core vocabularies

- **mineralSKOS.ttl** — SKOS vocabulary of mineral species (6,299 concepts). Includes links to Mindat, webmineral, Handbook of Mineralogy. Mapping to URIs from Wikidata, Mindat, and Geological Survey of Queensland vocabularies. Properties include RRUFF IDs, crystal system, elements present, chemical formulas, locality count, Fleischer and Strunz groups. See `MineralSKOS-readme.md` for compilation details.

- **SamplingMethods.ttl** — Vocabulary of material sample collection methods. 154 concepts.

- **SESAR_materials_extension.ttl** — Lithology/material types, rooted in iSamples material vocabulary and iSamples Earth Science material type extension vocabulary.

- **SESAR_sampled_feature_extension.ttl** — Extends the iSamples Sampled Feature Type vocabulary with concepts from GeoSciML event environment vocabulary, SESAR legacy data, and IMLGS vocabulary. 262 concepts.

- **SESAR_material_object_type_extension.ttl** — Material sample object types extending the iSamples material sample object type vocabulary.

## Sampling method vocabularies (`samplingMethods/`)

- **samplePreparation_GSQ.ttl** — Queensland Geological Survey sample preparation methods.
- **sampling-method_GAv1-0.ttl** — Geoscience Australia sampling methods (v1.0).
- **sampling-method_GAv1-0original.ttl** — Original version of the GA sampling methods vocabulary.
- **SamplePreparationSeaDataNet.ttl** — SeaDataNet sample preparation device categories (from NERC vocabulary server).
- **SampleCollectionSeaDataNet.ttl** — SeaDataNet sample collection device categories (from NERC vocabulary server).

## Archive (`archive/`)

- **mineralSKOStrunc.ttl** — Truncated version of the mineral SKOS vocabulary (previous version).
