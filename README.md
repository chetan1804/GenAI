# GenAI

A lightweight generative AI workspace for experimenting with chat models, embeddings, and small app prototypes.

## Overview

This repository contains example tooling for building and testing generative AI workflows using OpenAI, Hugging Face, Google Gemini, Groq, Mistral, and LangChain.

## Requirements

- Python 3.14 or newer
- A virtual environment (`venv`, `.venv`, or similar)
- API keys stored in a `.env` file or environment variables for services you use

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you want to install the project as an editable package:

```bash
pip install -e .
```

## Usage

- Use the scripts and sample code in `chatmodels/` to experiment with chat model integrations.
- Use `embeddingmodels/` for embedding model experiments.
- Use `cinesage/` for small UI or core experimentation workflows.
- The package entrypoint is defined in `pyproject.toml` as `genai = "genai:main"`.

> Note: Run API examples only after configuring your credentials in `.env` or your environment.

## Project Structure

- `chatmodels/` — chat integration examples and helper code for language model experiments.
- `cinesage/` — core and UI experimentation code.
- `embeddingmodels/` — embedding model examples and wrappers.
- `src/genai/` — package source with the main entrypoint.
- `pyproject.toml` — package metadata and dependency declarations.
- `requirements.txt` — dependency list for local installs.
- `README.md` — project overview and onboarding notes.

## Recommended Workflow

1. Create a `.env` file for keys like `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `HUGGINGFACE_API_KEY`, etc.
2. Activate your virtual environment.
3. Install dependencies.
4. Explore one of the example files under `chatmodels/`, `embeddingmodels/`, or `cinesage/`.
5. Update the `README.md` when adding new tools or new app entrypoints.

## Notes

- Keep secrets and API keys out of version control.
- Prefer environment variables for configuration.
- Update this file as the project grows.
