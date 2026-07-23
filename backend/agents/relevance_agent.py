import json
from ollama import chat


class RelevanceJudge:

    def __init__(self):
        self.model = "llama3.2"

    def evaluate(self, question: str, response: str):

        prompt = f"""
You are an AI Evaluation Judge.

Evaluate how relevant the AI response is to the user's question.

Question:
{question}

AI Response:
{response}

Scoring Guidelines:

0.90 - 1.00
The response directly and completely answers the question.

0.75 - 0.89
The response answers the question with only minor omissions.

0.50 - 0.74
The response is partially relevant.

0.00 - 0.49
The response is mostly irrelevant.

Return ONLY valid JSON.

Example:

{{
    "score":0.95,
    "reason":"The response directly answers the user's question and covers all important aspects."
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
                )
            }

        except Exception as e:

            return {
                "score": 0.0,
                "reason": f"Relevance Judge Error: {str(e)}"
            }