# Data Models

## Overview

The AI Evaluation Platform exchanges structured data between the frontend, backend, retrieval system, and vector database. The following data models are used throughout the application.

---

# Evaluation Request

The frontend sends an evaluation request to the backend.

Fields:

| Field | Type | Description |
|--------|------|-------------|
| question | string | User question |
| ai_response | string | AI generated response |
| reference_answer | string (optional) | Ground truth answer |

Example

```json
{
  "question": "When did Beyonce become famous?",
  "ai_response": "Beyonce became famous in the late 1990s.",
  "reference_answer": "She became famous in the late 1990s."
}
```

---

# Evaluation Response

Returned by the backend.

| Field | Type |
|--------|------|
| retrieved_context | string |
| report_file | string |
| relevance_score | float |
| accuracy_score | float |
| hallucination_score | float |
| completeness_score | float |
| overall_score | float |
| verdict | string |

Example

```json
{
  "retrieved_context":"...",
  "report_file":"evaluation_report.pdf",
  "relevance_score":1.0,
  "accuracy_score":0.82,
  "hallucination_score":0.08,
  "completeness_score":1.0,
  "overall_score":0.88,
  "verdict":"Good"
}
```

---

# Knowledge Base Model

Each processed record contains:

| Field | Description |
|--------|-------------|
| question | Original question |
| context | Source context |
| answer | Ground truth answer |
| dataset | Dataset name |

---

# Chunk Model

Each chunk stored in ChromaDB contains:

- Question
- Context
- Answer
- Dataset

These chunks are converted into vector embeddings.

---

# Embedding Model

Embedding Model:

- all-MiniLM-L6-v2

Vector Database:

- ChromaDB

Similarity Search:

- Cosine Similarity

---

# Report Model

Generated PDF includes:

- Question
- AI Answer
- Reference Answer
- Retrieved Context
- Scores
- Final Verdict

---

# Summary

The system uses structured request and response models to ensure consistency across the frontend, backend, retrieval pipeline, and evaluation engine.