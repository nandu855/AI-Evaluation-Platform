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
    scores
):

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(
        Paragraph(
            "<b>AI Evaluation Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

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

    story.append(Spacer(1, 10))

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

    story.append(
        Paragraph(
            "<b>Evaluation Scores</b>",
            styles["Heading2"]
        )
    )

    for key, value in scores.items():

        story.append(
            Paragraph(
                f"{key} : {value}",
                styles["BodyText"]
            )
        )

    pdf.build(story)

    return filename