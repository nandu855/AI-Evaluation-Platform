from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

# Load embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


class RelevanceJudge:
    def evaluate(self, question: str, response: str):
        """
        Evaluates how relevant the AI response is to the user's question.
        """

        question_embedding = model.encode(question, convert_to_tensor=True)
        response_embedding = model.encode(response, convert_to_tensor=True)

        similarity = cos_sim(question_embedding, response_embedding).item()

        score = round(max(0.0, min(similarity, 1.0)), 2)

        if score >= 0.85:
            reason = "The response directly answers the user's question."
        elif score >= 0.65:
            reason = "The response is partially relevant to the user's question."
        else:
            reason = "The response is not sufficiently relevant to the user's question."

        return {
            "score": score,
            "reason": reason
        }