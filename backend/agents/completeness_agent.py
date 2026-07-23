import json
from ollama import chat


class CompletenessJudge:

    def __init__(self):
        self.model = "llama3.2"

    def evaluate(
        self,
        question,
        response,
        reference,
        retrieved_context
    ):

        prompt = f"""
You are an expert AI Evaluation Judge.

Your task is to determine whether the AI response completely answers the user's question.

Question:
{question}

AI Response:
{response}

Reference Answer:
{reference}

Retrieved Context:
{retrieved_context}

Instructions:

1. Identify the important aspects of the question.
2. Determine which aspects are covered.
3. Determine which aspects are missing.
4. Give a completeness score between 0 and 1.
5. Explain your reasoning.

Return ONLY valid JSON.

Example:

{{
    "score":0.82,
    "covered":[
        "Aspect 1",
        "Aspect 2"
    ],
    "missing":[
        "Aspect 3"
    ],
    "reason":"The answer covers the major concepts but misses one important point."
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

            # Remove markdown if LLM returns ```json
            if content.startswith("```"):
                content = (
                    content.replace("```json", "")
                    .replace("```", "")
                    .strip()
                )

            result = json.loads(content)

            score = float(result.get("score", 0.0))
            score = max(0.0, min(score, 1.0))

            return {

                "score": round(score, 2),

                "covered": result.get(
                    "covered",
                    []
                ),

                "missing": result.get(
                    "missing",
                    []
                ),

                "reason": result.get(
                    "reason",
                    "No explanation provided."
                )

            }

        except Exception as e:

            return {

                "score": 0.0,

                "covered": [],

                "missing": [],

                "reason": f"Completeness Judge Error: {str(e)}"

            }