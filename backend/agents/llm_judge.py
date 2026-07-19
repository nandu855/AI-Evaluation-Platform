from ollama import chat


class LLMJudge:

    def explain(
        self,
        question,
        response,
        reference,
        context
    ):

        prompt = f"""
You are an AI Evaluation Judge.

Question:
{question}

AI Response:
{response}

Reference Answer:
{reference}

Retrieved Context:
{context}

Evaluate the response.

Provide:

Relevance:
- Short explanation

Accuracy:
- Short explanation

Hallucination:
- Mention unsupported claims if any

Overall:
- Final assessment

Return ONLY plain text.
"""

        reply = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return reply["message"]["content"]