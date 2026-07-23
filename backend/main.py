from fastapi import FastAPI

from backend.models import (
    EvaluationRequest,
    EvaluationResponse
)

from backend.rag import retrieve_context
from backend.report import generate_report
from backend.agents.judge import Judge

app = FastAPI(
    title="AI Evaluation Platform",
    version="3.0.0"
)

judge = Judge()


@app.get("/")
def home():
    return {
        "message": "AI Evaluation Platform Running",
        "version": "Milestone 3"
    }


@app.post(
    "/evaluate",
    response_model=EvaluationResponse
)
def evaluate_answer(request: EvaluationRequest):

    # ------------------------------------
    # Retrieve Context using RAG
    # ------------------------------------

    context = retrieve_context(request.question)

    # ------------------------------------
    # Run all Judge Agents
    # ------------------------------------

    judge_results = judge.evaluate(
        question=request.question,
        response=request.ai_response,
        reference=request.reference_answer or "",
        retrieved_context=context
    )

    # ------------------------------------
    # Generate PDF Report
    # ------------------------------------

    report_file = generate_report(
        filename="evaluation_report.pdf",
        question=request.question,
        ai_answer=request.ai_response,
        reference_answer=request.reference_answer or "",
        retrieved_context=context,
        judge_results=judge_results
    )

    # ------------------------------------
    # Return API Response
    # ------------------------------------

    return {
        "retrieved_context": context,
        "report_file": report_file,
        "judge_results": judge_results
    }