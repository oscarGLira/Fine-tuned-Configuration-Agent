# Fine-tuned-Configuration-Agent

This repository contains datasets and scripts for working with requirements-configuration pairs derived from 82 processed documents, supporting fine-tuning and configuration automation tasks.

## Datasets

| Dataset | Description | Entries | Features|
|---------|-------------|---------|---------|
| Total requirements.csv | Comprehensive dataset created from 82 documents | 14,803 | requirement, configuration|
|requirements.csv | Smaller dataset for fine-tuning | 5,506 | requirement, configuration |
|requirements_cleaned | Cleaned dataset with null or invalid entries removed | 5,105 | requirement, configuration |
| requirements_questions | Questions-configurations dataset with rephrased questions | 5,097 | question, configuration |

## Scripts

| Script | Description |
|--------|-------------|
| PDFExtractor.py | This script extracts requirements and configurations directly from PDF files. It processes documents to generate entries for the requirements-configuration datasets. |
| datasetclean.py | Takes requirements.csv as input, filters out null or invalid entries, and generates requirements_cleaned, a cleaned version of the dataset. |
| questions_configruations.py | Processes requirements_cleaned to rephrase requirements into questions and refines configurations, generating the requirements_questions dataset for question-based configuration matching. |
