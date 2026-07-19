import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.agents.judge import Judge

judge = Judge()

test_cases = [
    {
        "question": "When did Beyonce become famous?",
        "response": "Beyonce became famous in the late 1990s as the lead singer of Destiny's Child.",
        "reference": "She became famous in the late 1990s.",
        "context": "Beyonce rose to fame during the late 1990s as the lead singer of Destiny's Child."
    },
    {
        "question": "Who developed the theory of relativity?",
        "response": "Albert Einstein developed the theory of relativity.",
        "reference": "Albert Einstein developed the theory of relativity.",
        "context": "Albert Einstein introduced the theory of relativity in the early 20th century."
    },
    {
        "question": "What is the capital of France?",
        "response": "The capital of France is Berlin.",
        "reference": "Paris is the capital of France.",
        "context": "Paris is the capital city of France."
    }
]

for i, case in enumerate(test_cases, start=1):
    print("=" * 60)
    print(f"Test Case {i}")
    print("=" * 60)

    result = judge.evaluate(
        question=case["question"],
        response=case["response"],
        reference=case["reference"],
        retrieved_context=case["context"]
    )

    print(result)
    print()