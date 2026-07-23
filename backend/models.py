from pydantic import BaseModel
from typing import List, Optional


# -----------------------------
# Request Models
# -----------------------------

class EvaluationRequest(BaseModel):
    question: str
    ai_response: str
    reference_answer: Optional[str] = ""


# -----------------------------
# Judge Result Models
# -----------------------------

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


class CompletenessJudgeResult(BaseModel):
    score: float
    covered: List[str]
    missing: List[str]
    reason: str


class JudgeResults(BaseModel):
    relevance: RelevanceJudgeResult
    accuracy: AccuracyJudgeResult
    hallucination: HallucinationJudgeResult
    completeness: CompletenessJudgeResult

    overall_score: float
    verdict: str
    summary: str

    llm_reasoning: str


# -----------------------------
# API Response
# -----------------------------

class EvaluationResponse(BaseModel):
    retrieved_context: str

    report_file: str

    judge_results: JudgeResults