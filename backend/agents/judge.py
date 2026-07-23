from backend.agents.relevance_agent import RelevanceJudge
from backend.agents.accuracy_agent import AccuracyJudge
from backend.agents.hallucination_agent import HallucinationJudge
from backend.agents.completeness_agent import CompletenessJudge
from backend.agents.verdict_agent import VerdictAgent
from backend.agents.llm_judge import LLMJudge


class Judge:

    def __init__(self):

        self.relevance_agent = RelevanceJudge()

        self.accuracy_agent = AccuracyJudge()

        self.hallucination_agent = HallucinationJudge()

        self.completeness_agent = CompletenessJudge()

        self.verdict_agent = VerdictAgent()

        self.llm_judge = LLMJudge()

    def evaluate(

        self,

        question,

        response,

        reference,

        retrieved_context

    ):

        # -----------------------------
        # Relevance
        # -----------------------------

        relevance = self.relevance_agent.evaluate(

            question,

            response

        )

        # -----------------------------
        # Accuracy
        # -----------------------------

        accuracy = self.accuracy_agent.evaluate(

            response,

            reference,

            retrieved_context

        )

        # -----------------------------
        # Hallucination
        # -----------------------------

        hallucination = self.hallucination_agent.evaluate(

            response,

            retrieved_context

        )

        # -----------------------------
        # Completeness
        # -----------------------------

        completeness = self.completeness_agent.evaluate(

            question,

            response,

            reference,

            retrieved_context

        )

        # -----------------------------
        # Final Verdict
        # -----------------------------

        verdict = self.verdict_agent.evaluate(

            relevance["score"],

            accuracy["score"],

            hallucination["score"],

            completeness["score"]

        )

        # -----------------------------
        # LLM Explanation
        # -----------------------------

        llm_reasoning = self.llm_judge.explain(

            question=question,

            response=response,

            reference=reference,

            context=retrieved_context,

            relevance=relevance,

            accuracy=accuracy,

            hallucination=hallucination,

            completeness=completeness,

            verdict=verdict

        )

        # -----------------------------
        # Return Results
        # -----------------------------

        return {

            "relevance": relevance,

            "accuracy": accuracy,

            "hallucination": hallucination,

            "completeness": completeness,

            "overall_score": verdict["overall_score"],

            "verdict": verdict["verdict"],

            "summary": verdict["summary"],

            "llm_reasoning": llm_reasoning

        }