from fastapi import (
    FastAPI,
    Body
)

from typing import (
    List,
    Dict
)

from backend.models import (
    EvaluationRequest,
    EvaluationResponse
)

from backend.rag import retrieve_context

from backend.report import generate_report

from backend.batch_report import (
    generate_batch_report
)

from backend.agents.judge import Judge


app = FastAPI(

    title="AI Evaluation Platform",

    version="4.0.0"

)

judge = Judge()


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

    # ----------------------------------------
    # Retrieve Context
    # ----------------------------------------

    context = retrieve_context(
        request.question
    )

    # ----------------------------------------
    # Judge Agents
    # ----------------------------------------

    judge_results = judge.evaluate(

        question=request.question,

        response=request.ai_response,

        reference=request.reference_answer or "",

        retrieved_context=context

    )

    # ----------------------------------------
    # Single PDF
    # ----------------------------------------

    report_file = generate_report(

        filename="evaluation_report.pdf",

        question=request.question,

        ai_answer=request.ai_response,

        reference_answer=request.reference_answer or "",

        retrieved_context=context,

        judge_results=judge_results

    )

    return {

        "retrieved_context": context,

        "report_file": report_file,

        "judge_results": judge_results

    }


# ==========================================================
# BATCH REPORT
# ==========================================================

@app.post(
    "/generate-batch-report"
)
def batch_report(
    results: List[Dict] = Body(...)
):
        try:

        generate_batch_report(

            filename="batch_evaluation_report.pdf",

            results=results

        )

        return {

            "status": "success",

            "message": "Batch Evaluation Report Generated Successfully",

            "report_file": "batch_evaluation_report.pdf"

        }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e)

        }