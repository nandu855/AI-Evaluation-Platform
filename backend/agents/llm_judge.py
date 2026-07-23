from ollama import chat


class LLMJudge:

    def __init__(self):
        self.model = "llama3.2"

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