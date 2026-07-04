from difflib import SequenceMatcher


def similarity(a, b):
    return SequenceMatcher(
        None,
        str(a).lower(),
        str(b).lower()
    ).ratio()


def keyword_overlap(text1, text2):

    words1 = set(str(text1).lower().split())
    words2 = set(str(text2).lower().split())

    if len(words1) == 0:
        return 0

    return len(words1 & words2) / len(words1)


def evaluate(
        question,
        ai_response,
        reference_answer,
        retrieved_context
):

    # -----------------------------
    # Relevance
    # -----------------------------
    relevance = keyword_overlap(
        question,
        retrieved_context
    )

    # -----------------------------
    # Accuracy
    # -----------------------------
    if reference_answer.strip():

        accuracy = (
            similarity(ai_response, reference_answer) * 0.7
            +
            keyword_overlap(ai_response, reference_answer) * 0.3
        )

    else:

        accuracy = (
            similarity(ai_response, retrieved_context) * 0.6
            +
            keyword_overlap(ai_response, retrieved_context) * 0.4
        )

    # -----------------------------
    # Hallucination
    # -----------------------------
    overlap = keyword_overlap(
        ai_response,
        retrieved_context
    )

    hallucination = max(
        0,
        1 - overlap
    )

    # -----------------------------
    # Completeness
    # -----------------------------
    if reference_answer.strip():

        completeness = min(
            len(ai_response) /
            max(len(reference_answer), 1),
            1.0
        )

    else:

        completeness = min(
            len(ai_response) /
            max(len(retrieved_context), 1),
            1.0
        )

    # -----------------------------
    # Overall Score
    # -----------------------------
    overall = (
        relevance * 0.20 +
        accuracy * 0.45 +
        (1 - hallucination) * 0.25 +
        completeness * 0.10
    )

    # -----------------------------
    # Verdict
    # -----------------------------
    if overall >= 0.90:
        verdict = "Excellent"

    elif overall >= 0.75:
        verdict = "Good"

    elif overall >= 0.55:
        verdict = "Average"

    else:
        verdict = "Poor"

    return {

        "relevance_score": round(relevance, 2),

        "accuracy_score": round(accuracy, 2),

        "hallucination_score": round(hallucination, 2),

        "completeness_score": round(completeness, 2),

        "overall_score": round(overall, 2),

        "verdict": verdict

    }