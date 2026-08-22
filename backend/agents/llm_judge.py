import os

from ollama import chat


class LLMJudge:

    def __init__(self):
        self.provider = os.getenv(
            "LLM_PROVIDER",
            "ollama"
        )

        self.model = os.getenv(
            "LLM_MODEL",
            "llama3.2"
        )

        self.openai_client = None

        if self.provider == "openai":
            from openai import OpenAI

            api_key = os.getenv("OPENAI_API_KEY")

            if not api_key:
                raise ValueError(
                    "OPENAI_API_KEY is required when "
                    "LLM_PROVIDER=openai"
                )

            self.openai_client = OpenAI(
                api_key=api_key
            )

    def explain(
        self,
        question,
        response,
        reference,
        context,
        relevance,
        accuracy,
        hallucination,
        completeness,
        verdict
    ):

        prompt = f"""
You are an expert AI Evaluation Judge.

You have already received evaluation results from four specialized judge agents.

Generate a professional evaluation report.

Question:
{question}

AI Response:
{response}

Reference Answer:
{reference}

Retrieved Context:
{context}

---------------------------------------

Relevance

Score:
{relevance["score"]}

Reason:
{relevance["reason"]}

---------------------------------------

Accuracy

Score:
{accuracy["score"]}

Reason:
{accuracy["reason"]}

Evidence:
{accuracy["evidence"]}

---------------------------------------

Hallucination

Score:
{hallucination["score"]}

Reason:
{hallucination["reason"]}

Unsupported Claims:
{hallucination["unsupported_claims"]}

---------------------------------------

Completeness

Score:
{completeness["score"]}

Covered:
{completeness["covered"]}

Missing:
{completeness["missing"]}

Reason:
{completeness["reason"]}

---------------------------------------

Overall Score

{verdict["overall_score"]}

Verdict

{verdict["verdict"]}

Summary

{verdict["summary"]}

---------------------------------------

Write a professional report using the following headings:

Overall Assessment

Strengths

Weaknesses

Suggestions for Improvement

Keep the response concise and readable.

Return ONLY plain text.
"""

        # --------------------------------------------------
        # LOCAL LLM - OLLAMA
        # --------------------------------------------------

        if self.provider == "ollama":

            reply = chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return reply["message"]["content"]

        # --------------------------------------------------
        # CLOUD LLM - OPENAI
        # --------------------------------------------------

        if self.provider == "openai":

            reply = self.openai_client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2
            )

            return reply.choices[0].message.content

        # --------------------------------------------------
        # INVALID PROVIDER
        # --------------------------------------------------

        raise ValueError(
            f"Unsupported LLM_PROVIDER: {self.provider}"
        )