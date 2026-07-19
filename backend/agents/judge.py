from backend.agents.relevance_agent import RelevanceJudge
from backend.agents.accuracy_agent import AccuracyJudge
from backend.agents.hallucination_agent import HallucinationJudge
from backend.agents.llm_judge import LLMJudge


class Judge:

    def __init__(self):

        self.relevance_agent = RelevanceJudge()
        self.accuracy_agent = AccuracyJudge()
        self.hallucination_agent = HallucinationJudge()
        self.llm_judge = LLMJudge()

    def evaluate(
        self,
        question,
        response,
        reference,
        retrieved_context
    ):

        relevance = self.relevance_agent.evaluate(
            question,
            response
        )

        accuracy = self.accuracy_agent.evaluate(
            response,
            reference,
            retrieved_context
        )

        hallucination = self.hallucination_agent.evaluate(
            response,
            retrieved_context
        )

        overall_score = round(
            (
                relevance["score"] +
                accuracy["score"] +
                hallucination["score"]
            ) / 3,
            2
        )

        if overall_score >= 0.85:
            verdict = "Excellent"

        elif overall_score >= 0.70:
            verdict = "Good"

        elif overall_score >= 0.50:
            verdict = "Fair"

        else:
            verdict = "Poor"

        llm_reasoning = self.llm_judge.explain(
            question,
            response,
            reference,
            retrieved_context
        )

        return {

            "relevance": relevance,

            "accuracy": accuracy,

            "hallucination": hallucination,

            "overall_score": overall_score,

            "verdict": verdict,

            "llm_reasoning": llm_reasoning

        }