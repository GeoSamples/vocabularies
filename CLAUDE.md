# CLAUDE.md

## Project overview

This repository contains SKOS vocabularies (RDF/Turtle) for the GeoSamples.org / SESAR sample registration system. It also functions as a GitHub Action that converts SKOS Turtle files to HTML documentation via a pipeline: Turtle → SQLite (navocab) → Markdown (vocab2mdCacheV2) → HTML (Quarto).

The generated HTML is published to GitHub Pages at https://geosamples.github.io/vocabularies/.

## Repository structure

- `vocabulary/` — Source SKOS Turtle (.ttl) files
  - `samplingMethods/` — Additional sampling/preparation vocabularies (GSQ, GA, SeaDataNet)
  - `archive/` — Old/truncated vocabulary files
- `tools/` — Python processing tools
  - `vocab.py` — CLI for loading TTL into SQLite via navocab
  - `vocab2mdCacheV2.py` — Generates Quarto-compatible Markdown from the SQLite cache
  - `navocab/` — Python package wrapping rdflib + rdflib-sqlalchemy for SKOS vocabulary access
- `docs/` — Generated HTML/Markdown output (deployed to gh-pages)
- `cache/` — SQLite database directory (transient, DB is created fresh each workflow run)
- `.github/actions/github_action_main.py` — Docker entrypoint that orchestrates the pipeline
- `.github/workflows/` — GitHub Actions workflow definitions
- `Dockerfile` — Builds the processing container (Python 3.12 + Quarto)
- `action.yml` — GitHub Action metadata (inputs: action, path, inputttl, inputvocaburi)

## GitHub Actions workflows

- **Process vocabularies** (`process_vocab.yml`) — Manual dispatch. Processes all vocabularies except mineralSKOS. Each vocabulary is processed with a fresh SQLite DB for isolation.
- **Process mineralSKOS** (`process_mineralSKOS.yml`) — Manual dispatch. Separate workflow for mineralSKOS due to its large size (~9MB, 6299 concepts, ~20 min processing time).
- **build** (`integration.yml`) — Runs on push to main/develop. Builds the Docker image and runs a smoke test with one vocabulary.
- **Test vocabularies** (`testdocs_process_vocab.yml`) — Manual dispatch. Tests the pipeline with a small subset of vocabularies.

## Processing pipeline

Each vocabulary is processed independently (fresh DB per vocab) to prevent ConceptScheme URI collisions (e.g., SeaDataNet files share the same ConceptScheme but have different top concepts):

1. Delete SQLite cache DB
2. `vocab.py load <file.ttl> <conceptscheme-uri>` — parse Turtle, store in SQLite
3. `vocab2mdCacheV2.py <db> <conceptscheme-uri>` — query DB, generate Markdown
4. `quarto render <file.md> -t html` — render Markdown to HTML
5. Deploy HTML to gh-pages branch via JamesIves/github-pages-deploy-action

## Vocabulary SKOS patterns

The code handles several SKOS patterns:
- **Standard**: concepts use `skos:topConceptOf`, `skos:inScheme`, `skos:broader`
- **Inverse top concept**: ConceptScheme uses `skos:hasTopConcept` instead of concepts using `skos:topConceptOf`
- **No inScheme**: some vocabularies (GSQ) don't use `skos:inScheme` on concepts; `getNarrower` falls back to `skos:broader` only
- **Cross-scheme children**: SeaDataNet concepts may have `skos:inScheme` pointing to a different ConceptScheme than their parent; handled by the broader-only fallback

## Key constraints

- `inputttl` entries are pipe-delimited, no spaces, no file extensions. Subdirectory paths are allowed (e.g., `samplingMethods/samplePreparation_GSQ`).
- `inputvocaburi` entries are pipe-delimited, can be CURIEs (e.g., `sesrs:materialvocabulary`) or full URIs.
- The Dockerfile pins `python:3.12-slim` and `setuptools<81` because `rdflib-sqlalchemy` 0.5.4 requires `pkg_resources`.
- Output filenames use the basename of the input TTL (subdirectory paths are stripped).

## Common tasks

**Regenerate all vocabulary HTML (except mineralSKOS):**
Go to Actions → "Process vocabularies" → Run workflow

**Regenerate mineralSKOS HTML:**
Go to Actions → "Process mineralSKOS" → Run workflow

**Add a new vocabulary:**
1. Add the .ttl file to `vocabulary/` (or a subdirectory)
2. Add its filename (without .ttl) and ConceptScheme URI to `process_vocab.yml` (pipe-delimited, order must match)
3. Add a section to `docs/readme.md` with HTML and RDF source links
4. Trigger "Process vocabularies"
