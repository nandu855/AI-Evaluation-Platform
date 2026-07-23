import json
from ollama import chat


class AccuracyJudge:

    def __init__(self):
        self.model = "llama3.2"

    def evaluate(
        self,
        response: str,
        reference: str,
        retrieved_context: str
    ):

        prompt = f"""
You are an expert AI Evaluation Judge.

Evaluate the factual accuracy of the AI response.

AI Response:
{response}

Reference Answer:
{reference}

Retrieved Context:
{retrieved_context}

Instructions:

- Compare the AI response with both the reference answer and retrieved context.
- Determine whether the response is factually correct.
- Ignore wording differences if the meaning is correct.

Scoring Guidelines:

0.90 - 1.00
The response is factually correct and fully supported.

0.75 - 0.89
Mostly accurate with only minor inaccuracies.

0.50 - 0.74
Partially accurate but contains some factual mistakes.

0.00 - 0.49
Mostly inaccurate or unsupported.

Return ONLY valid JSON.

Example:

{{
    "score":0.96,
    "reason":"The response accurately matches both the reference answer and retrieved context.",
    "evidence":"The retrieved context supports the major claims."
}}
"""

        try:

            reply = chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            content = reply["message"]["content"].strip()

            if content.startswith("```"):
                content = (
                    content.replace("```json", "")
                    .replace("```", "")
                    .strip()
                )

            result = json.loads(content)

            score = float(result.get("score", 0))
            score = max(0.0, min(score, 1.0))

            return {
                "score": round(score, 2),
                "reason": result.get(
                    "reason",
                    "No reason provided."
                ),
                "evidence": result.get(
                    "evidence",
                    retrieved_context
                )
            }

        except Exception as e:

            return {
                "score": 0.0,
                "reason": f"Accuracy Judge Error: {str(e)}",
                "evidence": retrieved_context
            }