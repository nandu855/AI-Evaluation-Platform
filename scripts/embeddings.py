import os
import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer

print("=" * 60)
print("AI Evaluation Platform - Embedding Generator")
print("=" * 60)

# ---------------------------------------------------
# Load chunks
# ---------------------------------------------------
print("\nLoading chunks...")

df = pd.read_csv("datasets/chunks/chunks.csv")

# Clean data
df = df.dropna(subset=["chunk"])

df["chunk"] = df["chunk"].astype(str)
df["question"] = df["question"].fillna("").astype(str)
df["answer"] = df["answer"].fillna("").astype(str)
df["dataset"] = df["dataset"].fillna("").astype(str)

total = len(df)

print(f"Total Chunks : {total}")

# ---------------------------------------------------
# Load embedding model
# ---------------------------------------------------
print("\nLoading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model Loaded Successfully!")

# ---------------------------------------------------
# Connect ChromaDB
# ---------------------------------------------------
os.makedirs("vector_db", exist_ok=True)

client = chromadb.PersistentClient(path="vector_db")

collection = client.get_or_create_collection(
    name="knowledge_base"
)

# ---------------------------------------------------
# Resume from previous run
# ---------------------------------------------------
already_indexed = collection.count()

print(f"\nAlready Indexed : {already_indexed}")

if already_indexed >= total:
    print("\nEverything is already indexed.")
    exit()

# ---------------------------------------------------
# Generate embeddings
# ---------------------------------------------------
BATCH_SIZE = 128

print("\nGenerating embeddings...\n")

for start in range(already_indexed, total, BATCH_SIZE):

    batch = df.iloc[start:start + BATCH_SIZE]

    texts = batch["chunk"].tolist()

    embeddings = model.encode(
        texts,
        batch_size=32,
        show_progress_bar=False,
        convert_to_numpy=True
    )

    collection.add(
        ids=[str(i) for i in batch.index],
        embeddings=embeddings.tolist(),
        documents=texts,
        metadatas=[
            {
                "question": row["question"],
                "answer": row["answer"],
                "dataset": row["dataset"]
            }
            for _, row in batch.iterrows()
        ]
    )

    print(f"{min(start + BATCH_SIZE, total)}/{total} completed")

print("\n" + "=" * 60)
print("Vector Database Created Successfully!")
print("=" * 60)