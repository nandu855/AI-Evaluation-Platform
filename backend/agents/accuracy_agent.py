from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


class AccuracyJudge:
    def evaluate(self, response: str, reference: str, retrieved_context: str):
        """
        Evaluates factual accuracy of the AI response.
        """

        response_embedding = model.encode(response, convert_to_tensor=True)
        reference_embedding = model.encode(reference, convert_to_tensor=True)
        context_embedding = model.encode(retrieved_context, convert_to_tensor=True)

        reference_similarity = cos_sim(response_embedding, reference_embedding).item()
        context_similarity = cos_sim(response_embedding, context_embedding).item()

        score = round((reference_similarity + context_similarity) / 2, 2)

        score = max(0.0, min(score, 1.0))

        if score >= 0.85:
            reason = "The response is factually accurate and supported by the reference answer and retrieved context."
        elif score >= 0.65:
            reason = "The response is mostly accurate but could be more precise."
        else:
            reason = "The response is not well supported by the reference answer or retrieved context."

        return {
            "score": score,
            "reason": reason,
            "evidence": retrieved_context
        }