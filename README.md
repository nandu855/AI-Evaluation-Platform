# 🤖 AI Evaluation Platform

> A Multi-Agent AI Evaluation Platform that assesses AI-generated responses using **Retrieval-Augmented Generation (RAG)** and specialized **LLM-based Judge Agents** for explainable, reliable, and comprehensive evaluation.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Ollama](https://img.shields.io/badge/Ollama-Llama3.2-orange)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

# 📖 Overview

The **AI Evaluation Platform** is designed to evaluate AI-generated responses using a **multi-agent architecture** powered by **Llama 3.2** and **Retrieval-Augmented Generation (RAG)**.

Unlike traditional evaluation systems that rely solely on similarity metrics, this platform employs specialized AI Judge Agents to assess multiple quality dimensions, generate explainable reasoning, and provide a final evaluation verdict.

The platform includes:

- AI-powered evaluation
- RAG-based knowledge retrieval
- Multi-Agent architecture
- Explainable AI reasoning
- PDF report generation
- Batch evaluation of responses

---

# ✨ Features

## 🔍 Retrieval-Augmented Generation (RAG)

- Semantic document retrieval
- ChromaDB vector database
- Sentence Transformer embeddings
- Context-aware evaluation

---

## 🤖 AI Judge Agents

The platform consists of four specialized evaluation agents.

### 🟢 Relevance Judge
Evaluates whether the AI response directly answers the user's question.

### 🔵 Accuracy Judge
Determines factual correctness using:

- Reference Answer
- Retrieved Context

### 🟠 Hallucination Judge
Detects unsupported or fabricated information that is not grounded in the retrieved context.

### 🟣 Completeness Judge
Checks whether the response covers all important aspects of the user's question.

---

## ⚖️ Verdict Agent

The Verdict Agent combines the outputs of all Judge Agents using weighted scoring to generate:

- Overall Score
- Final Verdict
- Evaluation Summary

Weight Distribution:

| Metric | Weight |
|---------|---------|
| Relevance | 25% |
| Accuracy | 35% |
| Hallucination | 20% |
| Completeness | 20% |

---

## 🧠 LLM Summary Agent

Generates a professional explanation including:

- Overall Assessment
- Strengths
- Weaknesses
- Suggestions for Improvement

---

## 📄 Report Generation

The platform automatically generates:

- PDF Evaluation Report
- JSON Evaluation Report

---

## 📂 Batch Evaluation

Evaluate multiple responses simultaneously using CSV upload.

Generated statistics include:

- Average Overall Score
- Average Relevance
- Average Accuracy
- Average Hallucination
- Average Completeness
- PASS Count
- FAIL Count

---

# 🏗️ System Architecture

```
                         User
                           │
                           ▼
                  Streamlit Frontend
                           │
                           ▼
                    FastAPI Backend
                           │
                           ▼
              Retrieval-Augmented Generation
                           │
                           ▼
                    Retrieved Context
                           │
                           ▼
                     Judge Manager
                           │
       ┌──────────┬──────────┬──────────┬──────────┐
       ▼          ▼          ▼          ▼
 Relevance    Accuracy   Hallucination Completeness
    Judge        Judge        Judge         Judge
       └──────────┴──────────┴──────────┴──────────┘
                           │
                           ▼
                     Verdict Agent
                           │
                           ▼
                    LLM Summary Agent
                           │
                           ▼
                PDF Report + JSON Response
```

---

# 📂 Project Structure

```
AI-Evaluation-Platform
│
├── backend
│   ├── agents
│   │   ├── relevance_agent.py
│   │   ├── accuracy_agent.py
│   │   ├── hallucination_agent.py
│   │   ├── completeness_agent.py
│   │   ├── verdict_agent.py
│   │   ├── llm_judge.py
│   │   └── judge.py
│   │
│   ├── main.py
│   ├── models.py
│   ├── rag.py
│   ├── report.py
│   └── ...
│
├── frontend
│   └── app.py
│
├── knowledge_base
├── vector_db
├── requirements.txt
└── README.md
```

---

# 🛠️ Technology Stack

## Backend

- Python
- FastAPI

## Frontend

- Streamlit

## AI & Machine Learning

- Ollama
- Llama 3.2
- Sentence Transformers

## Vector Database

- ChromaDB

## Report Generation

- ReportLab

## Version Control

- Git
- GitHub

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/nandu855/AI-Evaluation-Platform.git

cd AI-Evaluation-Platform
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download and install Ollama.

Pull the required model:

```bash
ollama pull llama3.2
```

Verify installation:

```bash
ollama list
```

---

# Run Backend

```bash
python -m uvicorn backend.main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Run Frontend

```bash
streamlit run frontend/app.py
```

---

# Batch Evaluation

Prepare a CSV file with the following columns:

```csv
question,ai_response,reference_answer
```

Upload the CSV from the **Batch Evaluation** tab to evaluate multiple responses simultaneously.

---

# Example Workflow

```
User Question
        │
        ▼
Retrieve Context (RAG)
        │
        ▼
Run AI Judge Agents
        │
        ▼
Generate Verdict
        │
        ▼
Generate LLM Explanation
        │
        ▼
Generate PDF & JSON Reports
```

---

# Future Enhancements

- Multi-LLM evaluation
- Human feedback integration
- Docker deployment
- Cloud deployment
- Authentication & user management
- Evaluation history dashboard
- REST API authentication
- Advanced analytics

---

# Author

**ANAND KUMAR BADARALA**

GitHub: https://github.com/nandu855

---

# License

This project is developed for educational and research purposes.