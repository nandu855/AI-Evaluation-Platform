# backend/config.py

import os


# ============================================================
# EMBEDDING MODEL
# ============================================================

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "all-MiniLM-L6-v2"
)


# ============================================================
# VECTOR DATABASE
# ============================================================

VECTOR_DB_PATH = os.getenv(
    "VECTOR_DB_PATH",
    "vector_db"
)


# ============================================================
# CHROMA COLLECTION
# ============================================================

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "knowledge_base"
)


# ============================================================
# NUMBER OF RETRIEVED RESULTS
# ============================================================

TOP_K_RESULTS = int(
    os.getenv(
        "TOP_K_RESULTS",
        "5"
    )
)