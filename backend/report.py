from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    filename,
    question,
    ai_answer,
    reference_answer,
    retrieved_context,
    judge_results
):

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(filename)

    story = []

    # -----------------------------------
    # Title
    # -----------------------------------

    story.append(
        Paragraph(
            "<b>AI Evaluation Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    # -----------------------------------
    # Question
    # -----------------------------------

    story.append(
        Paragraph(
            f"<b>Question:</b><br/>{question}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 10))

    story.append(
        Paragraph(
            f"<b>AI Generated Answer:</b><br/>{ai_answer}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 10))

    story.append(
        Paragraph(
            f"<b>Reference Answer:</b><br/>{reference_answer}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 15))

    # -----------------------------------
    # Retrieved Context
    # -----------------------------------

    story.append(
        Paragraph(
            "<b>Retrieved Context</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            retrieved_context,
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    # -----------------------------------
    # Judge Scores
    # -----------------------------------

    story.append(
        Paragraph(
            "<b>Judge Agent Results</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Relevance Score : {judge_results['relevance']['score']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Reason : {judge_results['relevance']['reason']}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            f"Accuracy Score : {judge_results['accuracy']['score']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Reason : {judge_results['accuracy']['reason']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Evidence : {judge_results['accuracy']['evidence']}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            f"Hallucination Score : {judge_results['hallucination']['score']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Reason : {judge_results['hallucination']['reason']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Unsupported Claims : {', '.join(judge_results['hallucination']['unsupported_claims'])}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            f"Completeness Score : {judge_results['completeness']['score']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Covered : {', '.join(judge_results['completeness']['covered'])}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Missing : {', '.join(judge_results['completeness']['missing'])}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Reason : {judge_results['completeness']['reason']}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 15))

    # -----------------------------------
    # Final Verdict
    # -----------------------------------

    story.append(
        Paragraph(
            "<b>Final Evaluation</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Overall Score : {judge_results['overall_score']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Verdict : {judge_results['verdict']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Summary : {judge_results['summary']}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 15))

    # -----------------------------------
    # LLM Explanation
    # -----------------------------------

    story.append(
        Paragraph(
            "<b>LLM Evaluation</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            judge_results["llm_reasoning"].replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    pdf.build(story)

    return filename