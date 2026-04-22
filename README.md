# Vocabularies For GeoSamples.org

Vocabularies to support the SESAR sample registration system. The authoritative source files are SKOS RDF vocabularies serialized using Turtle syntax, located in the `vocabulary/` directory.

HTML view of vocabularies is available at https://geosamples.github.io/vocabularies.

## Vocabularies

### SESAR core vocabularies (`vocabulary/`)

| File | Description | ConceptScheme URI |
|------|-------------|-------------------|
| `SESAR_materials_extension.ttl` | Lithology/material types extending the iSamples material vocabulary | `sesrs:materialvocabulary` |
| `SESAR_sampled_feature_extension.ttl` | Geologic, physiographic, and environmental features extending iSamples Sampled Feature Type | `sessf:sfvocabulary` |
| `SamplingMethods.ttl` | Material sample collection methods (154 concepts) | `secm:samplingmethods` |
| `SESAR_material_object_type_extension.ttl` | Material sample object types extending iSamples | `sesot:objecttypevocabulary` |
| `mineralSKOS.ttl` | Mineral species vocabulary (6,299 concepts) with links to Mindat, RRUFF, Wikidata | `gcmin:conceptScheme` |

### Sampling method vocabularies (`vocabulary/samplingMethods/`)

| File | Description | ConceptScheme URI |
|------|-------------|-------------------|
| `samplePreparation_GSQ.ttl` | Queensland Geological Survey sample preparation methods | `http://linked.data.gov.au/def/sample-preparation-methods` |
| `sampling-method_GAv1-0.ttl` | Geoscience Australia sampling methods | `http://pid.geoscience.gov.au/def/voc/ga/samplingmethod` |
| `SamplePreparationSeaDataNet.ttl` | SeaDataNet sample preparation device categories | `http://vocab.nerc.ac.uk/scheme/SDNDEV/current` (top concept: ICAT02) |
| `SampleCollectionSeaDataNet.ttl` | SeaDataNet sample collection device categories | `http://vocab.nerc.ac.uk/scheme/SDNDEV/current` (top concept: ICAT01) |

## Processing pipeline

The repository doubles as a GitHub Action that converts SKOS Turtle files to HTML documentation:

**Turtle (.ttl) → SQLite (navocab/rdflib-sqlalchemy) → Markdown (vocab2mdCacheV2.py) → HTML (Quarto)**

Each vocabulary is processed independently with a fresh SQLite database to prevent data from different vocabularies interfering with each other. This is important for files like the SeaDataNet vocabularies that share the same ConceptScheme URI but have different top concepts.

### SKOS patterns handled

The vocabularies in this repository use several different SKOS patterns. The processing tools handle all of these:

- **Standard hierarchy**: Concepts use `skos:topConceptOf`, `skos:inScheme`, and `skos:broader` to establish hierarchy within a single ConceptScheme.
- **Inverse top concept declaration**: Some vocabularies (GSQ, SeaDataNet) declare top concepts using `skos:hasTopConcept` on the ConceptScheme rather than `skos:topConceptOf` on the concepts.
- **No `skos:inScheme`**: Some vocabularies (GSQ) don't use `skos:inScheme` on individual concepts. The code falls back to following `skos:broader` relationships regardless of scheme membership.
- **Cross-scheme children**: SeaDataNet concepts may have `skos:inScheme` pointing to a different ConceptScheme than their parent. The broader-only fallback handles this.

## GitHub Actions workflows

| Workflow | Trigger | Description |
|----------|---------|-------------|
| **Process vocabularies** (`process_vocab.yml`) | Manual | Generates HTML for all vocabularies except mineralSKOS |
| **Process mineralSKOS** (`process_mineralSKOS.yml`) | Manual | Generates HTML for mineralSKOS only (~20 min due to size) |
| **build** (`integration.yml`) | Push to main/develop | Docker build verification and smoke test |
| **Test vocabularies** (`testdocs_process_vocab.yml`) | Manual | Tests pipeline with a small vocabulary subset |

## Adding a new vocabulary

1. Add the `.ttl` file to `vocabulary/` (or `vocabulary/samplingMethods/`)
2. Add its filename (without `.ttl` extension) and ConceptScheme URI to the pipe-delimited `inputttl` and `inputvocaburi` lists in `process_vocab.yml`. Subdirectory paths are supported (e.g., `samplingMethods/myVocab`). Order must match between the two lists.
3. Add a section to `docs/readme.md` with links to the HTML page and RDF source file
4. Trigger the "Process vocabularies" workflow from the Actions tab

## Implementation details

- **Docker image**: `python:3.12-slim` with Quarto, rdflib, rdflib-sqlalchemy
- **Entry point**: `.github/actions/github_action_main.py`
- **Tools**: `tools/vocab.py` (CLI for DB loading), `tools/vocab2mdCacheV2.py` (markdown generation), `tools/navocab/` (SKOS/rdflib wrapper)
- **Dependencies**: `setuptools<81` is pinned because `rdflib-sqlalchemy` 0.5.4 requires `pkg_resources`
- **GitHub Pages**: Serves from the `/docs` directory on the `gh-pages` branch
