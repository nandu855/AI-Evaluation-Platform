class VerdictAgent:

    def __init__(self):

        # Weight distribution
        self.weights = {

            "relevance": 0.25,
            "accuracy": 0.35,
            "hallucination": 0.20,
            "completeness": 0.20

        }

    def evaluate(

        self,

        relevance,

        accuracy,

        hallucination,

        completeness

    ):

        overall_score = round(

            (
                relevance * self.weights["relevance"] +

                accuracy * self.weights["accuracy"] +

                hallucination * self.weights["hallucination"] +

                completeness * self.weights["completeness"]

            ),

            2

        )

        # Final Verdict

        if overall_score >= 0.85:

            verdict = "PASS"

        elif overall_score >= 0.65:

            verdict = "Needs Improvement"

        else:

            verdict = "FAIL"

        # Summary

        strengths = []
        weaknesses = []

        if relevance >= 0.80:
            strengths.append("high relevance")
        else:
            weaknesses.append("low relevance")

        if accuracy >= 0.80:
            strengths.append("good factual accuracy")
        else:
            weaknesses.append("accuracy issues")

        if hallucination >= 0.80:
            strengths.append("minimal hallucination")
        else:
            weaknesses.append("hallucinated content")

        if completeness >= 0.80:
            strengths.append("complete answer")
        else:
            weaknesses.append("missing important information")

        if strengths:

            summary = (
                "Strengths: "
                + ", ".join(strengths)
            )

            if weaknesses:

                summary += ". Weaknesses: " + ", ".join(weaknesses)

        else:

            summary = (
                "The response needs improvement across all evaluation dimensions."
            )

        return {

            "overall_score": overall_score,

            "verdict": verdict,

            "summary": summary

        }