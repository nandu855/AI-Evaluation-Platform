import re

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


class HallucinationJudge:
    def evaluate(self, response: str, retrieved_context: str):
        """
        Detects unsupported claims in the AI response.
        """

        # Split response into individual sentences
        sentences = [
            s.strip()
            for s in re.split(r"[.!?]", response)
            if s.strip()
        ]

        context_embedding = model.encode(
            retrieved_context,
            convert_to_tensor=True
        )

        unsupported_claims = []

        for sentence in sentences:

            sentence_embedding = model.encode(
                sentence,
                convert_to_tensor=True
            )

            similarity = cos_sim(
                sentence_embedding,
                context_embedding
            ).item()

            if similarity < 0.60:
                unsupported_claims.append(sentence)

        if len(sentences) == 0:
            score = 1.0
        else:
            score = round(
                1 - (len(unsupported_claims) / len(sentences)),
                2
            )

        if score >= 0.90:
            reason = "No hallucinated content detected."
        elif score >= 0.70:
            reason = "Minor unsupported information detected."
        else:
            reason = "Multiple unsupported claims detected."

        return {
            "score": score,
            "reason": reason,
            "unsupported_claims": unsupported_claims
        }