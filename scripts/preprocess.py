import json
import pandas as pd
import os

# ----------------------------
# Configuration
# ----------------------------
MAX_SQUAD = 10000
MAX_TRUTHFULQA = 500

# ----------------------------
# Create processed folder
# ----------------------------
os.makedirs("datasets/processed", exist_ok=True)

# ----------------------------
# Process SQuAD
# ----------------------------
print("Processing SQuAD...")

with open("datasets/squad/train-v2.0.json", "r", encoding="utf-8") as f:
    squad = json.load(f)

rows = []

for article in squad["data"]:
    for paragraph in article["paragraphs"]:

        context = paragraph["context"]

        for qa in paragraph["qas"]:

            question = qa["question"]

            answer = ""
            if len(qa["answers"]) > 0:
                answer = qa["answers"][0]["text"]

            rows.append({
                "question": question,
                "context": context,
                "answer": answer,
                "dataset": "SQuAD"
            })

squad_df = pd.DataFrame(rows)

# Limit dataset size
squad_df = squad_df.head(MAX_SQUAD)

print("SQuAD Records :", len(squad_df))

# ----------------------------
# Process TruthfulQA
# ----------------------------
print("Processing TruthfulQA...")

truth_df = pd.read_csv("datasets/truthfulqa/TruthfulQA.csv")

truth_df = truth_df.rename(columns={
    "Question": "question",
    "Best Answer": "answer"
})

truth_df["context"] = ""
truth_df["dataset"] = "TruthfulQA"

truth_df = truth_df[
    ["question", "context", "answer", "dataset"]
]

# Limit dataset size
truth_df = truth_df.head(MAX_TRUTHFULQA)

print("TruthfulQA Records :", len(truth_df))

# ----------------------------
# Merge
# ----------------------------
combined = pd.concat(
    [squad_df, truth_df],
    ignore_index=True
)

combined.to_csv(
    "datasets/processed/knowledge_base.csv",
    index=False
)

print("=" * 60)
print("Knowledge Base Created Successfully!")
print("Total Records :", len(combined))
print("=" * 60)