import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from backend.agents.judge import Judge

judge = Judge()

question = "What is Artificial Intelligence?"

answer = (
    "Artificial Intelligence is the simulation "
    "of human intelligence by machines."
)

reference = answer

context = answer

print("=" * 60)
print("Scoring Consistency Validation")
print("=" * 60)

scores = []

for i in range(5):

    result = judge.evaluate(

        question=question,

        response=answer,

        reference=reference,

        retrieved_context=context

    )

    scores.append(result["overall_score"])

    print(f"Run {i+1}")

    print(f"Overall Score : {result['overall_score']}")

    print(f"Verdict : {result['verdict']}")

    print("-" * 60)

average = sum(scores) / len(scores)

print()

print("Average Score :", round(average, 2))

if max(scores) - min(scores) <= 0.05:

    print("PASS : Stable Scoring")

else:

    print("WARNING : Score Variation Detected")