# 🤖 AI Evaluation Platform

An AI Evaluation Platform built using **FastAPI**, **Streamlit**, **ChromaDB**, and **Sentence Transformers** to evaluate AI-generated responses using a Retrieval-Augmented Generation (RAG) pipeline.

---

# Features

- AI response evaluation
- Retrieval-Augmented Generation (RAG)
- Semantic vector search using ChromaDB
- Reference knowledge base using SQuAD and TruthfulQA
- Multiple evaluation metrics
- PDF evaluation report generation
- Interactive Streamlit dashboard
- FastAPI REST API

---

# System Architecture

```
                User
                  │
                  ▼
          Streamlit Frontend
                  │
                  ▼
            FastAPI Backend
                  │
      ┌───────────┴───────────┐
      ▼                       ▼
 Retrieval Module      Evaluation Engine
      │                       │
      ▼                       ▼
     ChromaDB          Scoring Module
      │
      ▼
 Sentence Transformer
      │
      ▼
 Knowledge Base
(SQuAD + TruthfulQA)
```

---

# Tech Stack

## Backend

- FastAPI
- Uvicorn

## Frontend

- Streamlit

## Vector Database

- ChromaDB

## Embedding Model

- Sentence Transformers
- all-MiniLM-L6-v2

## Dataset

- SQuAD v2.0
- TruthfulQA

## Language

- Python 3.11

---

# Project Structure

```
AI-Evaluation-Platform
│
├── backend
│   ├── main.py
│   ├── rag.py
│   ├── scorer.py
│   ├── report.py
│   ├── config.py
│   └── models.py
│
├── frontend
│   └── app.py
│
├── scripts
│   ├── preprocess.py
│   ├── chunking.py
│   ├── embeddings.py
│   └── retrieve.py
│
├── datasets
│
├── vector_db
│
├── docs
│
├── images
│
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository.

```bash
git clone https://github.com/<your-username>/AI-Evaluation-Platform.git
```

Open the project.

```bash
cd AI-Evaluation-Platform
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Run Backend

```bash
uvicorn backend.main:app
```

---

# Run Frontend

```bash
streamlit run frontend/app.py
```

---

# API Endpoint

## Evaluate

POST

```
/evaluate
```

Example Request

```json
{
  "question": "When did Beyonce become famous?",
  "ai_response": "Beyonce became famous in the late 1990s.",
  "reference_answer": "She became famous in the late 1990s."
}
```

---

# Evaluation Metrics

- Relevance
- Accuracy
- Hallucination
- Completeness
- Overall Score

---

# Future Improvements

- Semantic evaluation using LLMs
- Cross-encoder reranking
- Advanced hallucination detection
- RAGAS integration
- TruLens integration
- Interactive analytics dashboard

---

# Author

Anand

---

# License

This project is developed for academic and educational purposes.