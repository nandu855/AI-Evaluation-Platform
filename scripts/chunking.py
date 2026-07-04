import pandas as pd
import os

df = pd.read_csv(
    "datasets/processed/knowledge_base.csv",
    low_memory=False
)

CHUNK_SIZE = 500

chunks = []

print("Creating chunks...")

for _, row in df.iterrows():

    question = str(row["question"])

    context = str(row["context"])

    answer = str(row["answer"])

    dataset = str(row["dataset"])

    if context.strip() == "" or context == "nan":
        context = answer

    document = (
        f"Question:\n{question}\n\n"
        f"Context:\n{context}\n\n"
        f"Answer:\n{answer}"
    )

    for i in range(0, len(document), CHUNK_SIZE):

        chunk = document[i:i + CHUNK_SIZE]

        chunks.append({
            "question": question,
            "chunk": chunk,
            "answer": answer,
            "dataset": dataset
        })

chunk_df = pd.DataFrame(chunks)

os.makedirs("datasets/chunks", exist_ok=True)

chunk_df.to_csv(
    "datasets/chunks/chunks.csv",
    index=False
)

print("=" * 60)
print("Chunking Completed Successfully!")
print("Total Chunks:", len(chunk_df))
print("=" * 60)