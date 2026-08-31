# RACE — Recursive AI Chunking Engine

RACE (Recursive AI Chunking Engine) is a hands-on learning project that demonstrates document text extraction and recursive text chunking using LangChain's `RecursiveCharacterTextSplitter`. It explores how chunk size and chunk overlap can be used to divide large text into manageable chunks for downstream AI applications such as embeddings, semantic search, and Retrieval-Augmented Generation (RAG).

## Repository Contents

This **RACE** repository contains the project in both **Jupyter Notebook (`.ipynb`) and Python (`.py`) formats**.

- **`langchain_recursive_text_chunking.ipynb`** — Interactive notebook containing the original step-by-step implementation.
- **`src/*.py`** — Modular Python files created from the notebook's code sequence for easier reuse and understanding.

Both formats are maintained so the project can be learned interactively through the notebook or explored through Python modules.

## Python Files

```text
src/
├── 01_installation.py
├── 02_pdf_extraction.py
├── 03_recursive_text_splitter.py
└── 04_chunking_demo.py
```

The modules follow the notebook workflow: dependency installation → PDF text extraction → recursive text splitting → chunking demonstration.

## Key Concepts

- Recursive Character Text Splitting
- Chunk Size
- Chunk Overlap
- PDF Text Extraction
- Document Preprocessing
- Preparing Text for Embeddings and RAG

## Technologies

- Python
- LangChain Text Splitters
- `RecursiveCharacterTextSplitter`
- pypdf
- Jupyter Notebook / Google Colab

## Purpose

RACE is designed as a learning-focused repository for understanding how recursive text chunking works and why effective chunking is an important preprocessing step in modern AI and RAG pipelines.

## Getting Started

Install the required packages:

```bash
pip install -q pypdf langchain-text-splitters
```

You can run the notebook interactively or use the Python modules in `src/`.

## Project Status

This repository is part of a hands-on AI learning project focused on document preprocessing and text chunking for downstream AI applications.

## License

This project is intended for educational and learning purposes.
