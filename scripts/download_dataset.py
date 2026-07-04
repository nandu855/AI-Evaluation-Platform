from datasets import load_dataset
import os

# Create datasets folder
os.makedirs("datasets", exist_ok=True)

print("Downloading SQuAD...")
squad = load_dataset("squad")

print("Downloading TruthfulQA...")
truthfulqa = load_dataset("truthful_qa", "generation")

print("Saving datasets...")

squad.save_to_disk("datasets/squad")
truthfulqa.save_to_disk("datasets/truthfulqa")

print("Datasets downloaded successfully!")