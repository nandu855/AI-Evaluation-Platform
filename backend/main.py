from fastapi import FastAPI, Body
from typing import List, Dict

from backend.models import (
    EvaluationRequest,
    EvaluationResponse
)

from backend.rag import retrieve_context
from backend.report import generate_report
from backend.batch_report import generate_batch_report
from backend.agents.judge import Judge


app = FastAPI(
    title="AI Evaluation Platform",
    version="4.0.0"
)

judge = Judge()


# ==========================================================
# HOME
# ==========================================================

@app.get("/")
def home():

    return {
        "message": "AI Evaluation Platform Running",
        "version": "Milestone 4"
    }


# ==========================================================
# SINGLE EVALUATION
# ==========================================================

@app.post(
    "/evaluate",
    response_model=EvaluationResponse
)
def evaluate_answer(
    request: EvaluationRequest
):

    # ------------------------------------------------------
    # Retrieve Context using RAG
    # ------------------------------------------------------

    context = retrieve_context(
        request.question
    )

    # ------------------------------------------------------
    # Run Judge Agents
    # ------------------------------------------------------

    judge_results = judge.evaluate(
        question=request.question,
        response=request.ai_response,
        reference=request.reference_answer or "",
        retrieved_context=context
    )

    # ------------------------------------------------------
    # Generate Single Evaluation PDF
    # ------------------------------------------------------

    report_file = generate_report(
        filename="evaluation_report.pdf",
        question=request.question,
        ai_answer=request.ai_response,
        reference_answer=request.reference_answer or "",
        retrieved_context=context,
        judge_results=judge_results
    )

    # ------------------------------------------------------
    # Return Response
    # ------------------------------------------------------

    return {
        "retrieved_context": context,
        "report_file": report_file,
        "judge_results": judge_results
    }


# ==========================================================
# BATCH PDF REPORT
# ==========================================================

@app.post(
    "/generate-batch-report"
)
def generate_batch_pdf(
    results: List[Dict] = Body(...)
):

    try:

        report_file = generate_batch_report(
            filename="batch_evaluation_report.pdf",
            results=results
        )

        return {
            "status": "success",
            "message": "Batch evaluation report generated successfully.",
            "report_file": report_file
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }