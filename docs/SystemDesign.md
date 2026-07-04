# System Design

# AI Evaluation Platform

## Overview

The AI Evaluation Platform is a Retrieval-Augmented Generation (RAG) based system that evaluates AI-generated answers using a reference knowledge base. The system accepts a question and an AI-generated response, retrieves the most relevant context from a vector database, evaluates the response across multiple quality dimensions, and returns a final verdict.

---

# High-Level Architecture

User

↓

Streamlit Frontend

↓

FastAPI Backend

↓

Evaluation Orchestrator

↓

RAG Retrieval Module

↓

ChromaDB Vector Database

↓

Sentence Transformer Embedding Model

↓

Knowledge Base (SQuAD + TruthfulQA)

---

# Modules

## 1. Evaluation Input Module

Responsibilities:

- Accept question
- Accept AI-generated response
- Accept optional reference answer
- Validate user input
- Send evaluation request to backend

Technology:

- Streamlit

---

## 2. Reference Knowledge Base

Responsibilities:

- Store benchmark datasets
- Store document chunks
- Generate embeddings
- Maintain vector database

Datasets:

- SQuAD
- TruthfulQA

Embedding Model:

- all-MiniLM-L6-v2

Vector Store:

- ChromaDB

---

## 3. Retrieval Module

Responsibilities:

- Convert user question into embedding
- Search vector database
- Retrieve Top-K relevant chunks
- Return retrieved context

---

## 4. Evaluation Module

The evaluation module computes:

- Relevance
- Accuracy
- Hallucination
- Completeness
- Overall Score

It also generates the final verdict.

---

## 5. Report Generation

Responsibilities:

- Generate PDF evaluation report
- Store evaluation summary
- Export evaluation results

---

# Orchestration Flow

User Input

↓

FastAPI API

↓

Retrieve Context

↓

Evaluate Response

↓

Generate Scores

↓

Generate Verdict

↓

Return Results

↓

Display Dashboard

---

# Data Flow

Question

↓

Embedding

↓

Vector Search

↓

Retrieved Context

↓

Score Calculation

↓

Final Verdict

↓

User Interface

---

# Design Goals

- Modular architecture
- Easy to extend
- Scalable
- Retrieval-based evaluation
- Explainable scoring
- Simple deployment