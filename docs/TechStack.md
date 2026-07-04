# Technology Stack

## Programming Language

- Python 3.11

---

# Backend

- FastAPI
- Uvicorn

Purpose:

- REST API development
- Evaluation endpoint
- Backend processing

---

# Frontend

- Streamlit

Purpose:

- User Interface
- Question submission
- Display evaluation scores
- Display retrieved context

---

# Embedding Model

Sentence Transformers

Model Used:

- all-MiniLM-L6-v2

Purpose:

- Generate vector embeddings
- Semantic similarity search

---

# Vector Database

ChromaDB

Purpose:

- Store document embeddings
- Perform similarity search
- Retrieve Top-K relevant chunks

---

# Knowledge Base

Datasets:

- SQuAD v2.0
- TruthfulQA

Purpose:

- Reference answers
- Retrieval source

---

# Data Processing

Libraries:

- Pandas
- JSON

Purpose:

- Dataset preprocessing
- Chunk creation

---

# Evaluation

Techniques Used:

- String similarity
- Keyword overlap
- Retrieval-based verification

Metrics:

- Relevance
- Accuracy
- Hallucination
- Completeness
- Overall Score

---

# PDF Report

Library:

- ReportLab

Purpose:

- Generate evaluation reports

---

# Version Control

- Git
- GitHub

Purpose:

- Source code management

---

# Development Tools

- Visual Studio Code
- PowerShell
- Git Bash

---

# Project Architecture

Frontend

↓

FastAPI Backend

↓

Retriever

↓

ChromaDB

↓

Knowledge Base

↓

Evaluation Engine

↓

Result Dashboard