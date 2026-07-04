from fastapi import FastAPI

from backend.models import (
    EvaluationRequest,
    EvaluationResponse
)

from backend.rag import retrieve_context

from backend.scorer import evaluate

from backend.report import generate_report

app = FastAPI(
    title="AI Evaluation Platform"
)


@app.get("/")
def home():

    return {
        "message": "AI Evaluation Platform Running"
    }


@app.post(
    "/evaluate",
    response_model=EvaluationResponse
)
def evaluate_answer(
        request: EvaluationRequest
):

    context = retrieve_context(
        request.question
    )

    scores = evaluate(

        request.question,

        request.ai_response,

        request.reference_answer,

        context

    )

    report_file = generate_report(

        filename="evaluation_report.pdf",

        question=request.question,

        ai_answer=request.ai_response,

        reference_answer=request.reference_answer,

        retrieved_context=context,

        scores=scores

    )

    return {

        "retrieved_context": context,

        "report_file": report_file,

        **scores

    }