# Vocabularies For GeoSamples.org

Vocabularies to support update to SESAR sample registration system

HTML view of vocabularies is available at https://geosamples.github.io/vocabularies. Vocabulary source files are in the vocabulary directory. 

## Vocabulary documents
This repository hosts vocabularies for populating SESAR sample descriptions.  The authoritative source files are rdf SKOS vocabularies serialized using Turtle syntax. These are in the **vocabulary** folder. The **docs** folder contains Markdown and HTML presentations of the vocabulary content.  

## Vocabulary github action

The vocabulary respository may be run as a GitHub action.  The `action.yml` (which is required to be located at the root of the repository) defines the action inputs and outputs.  

The action is run as a Docker image, and the image is built according to the instructions in the `Dockerfile` (which is also in the root of the repository, due to Docker's requirement that all things built into the image be located in the same directory).

### Testing
There is a test file at `.github/workflows/integration.yml`, which can be run manually using the workflow dispatch option.  It contains the necessary instruction to check out the repository and run it as a GitHub action.

### Implementation
The Docker entrypoint of the action is the python file located at `.github/actions/vocabularies/github_action_main.py`.  GitHub is responsible for converting the action parameters into environment variables that the script interprets.
