from pydantic import BaseModel
from typing import Optional


class EvaluationRequest(BaseModel):
    question: str
    ai_response: str
    reference_answer: Optional[str] = None


class EvaluationResponse(BaseModel):
    retrieved_context: str
    report_file: str

    relevance_score: float
    accuracy_score: float
    hallucination_score: float
    completeness_score: float

    overall_score: float

    verdict: str