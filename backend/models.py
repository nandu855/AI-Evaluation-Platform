from pydantic import BaseModel
from typing import Optional, List


class EvaluationRequest(BaseModel):
    question: str
    ai_response: str
    reference_answer: Optional[str] = ""


class RelevanceJudgeResult(BaseModel):
    score: float
    reason: str


class AccuracyJudgeResult(BaseModel):
    score: float
    reason: str
    evidence: str


class HallucinationJudgeResult(BaseModel):
    score: float
    reason: str
    unsupported_claims: List[str]


class JudgeResults(BaseModel):

    relevance: RelevanceJudgeResult

    accuracy: AccuracyJudgeResult

    hallucination: HallucinationJudgeResult

    overall_score: float

    verdict: str

    llm_reasoning: str


class EvaluationResponse(BaseModel):

    retrieved_context: str

    report_file: str

    relevance_score: float

    accuracy_score: float

    hallucination_score: float

    completeness_score: float

    overall_score: float

    verdict: str

    judge_results: JudgeResults