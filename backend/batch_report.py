from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def generate_batch_report(
    filename,
    results
):

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(filename)

    story = []

    # =====================================
    # Title
    # =====================================

    story.append(
        Paragraph(
            "<b>AI Evaluation Platform</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            "<b>Batch Evaluation Report</b>",
            styles["Heading1"]
        )
    )

    story.append(Spacer(1, 20))

    # =====================================
    # Statistics
    # =====================================

    total = len(results)

    pass_count = sum(
        1
        for row in results
        if row["Verdict"] == "PASS"
    )

    needs_count = sum(
        1
        for row in results
        if row["Verdict"] == "Needs Improvement"
    )

    fail_count = sum(
        1
        for row in results
        if row["Verdict"] == "FAIL"
    )

    avg_relevance = round(
        sum(
            row["Relevance"]
            for row in results
        ) / total,
        2
    )

    avg_accuracy = round(
        sum(
            row["Accuracy"]
            for row in results
        ) / total,
        2
    )

    avg_hallucination = round(
        sum(
            row["Hallucination"]
            for row in results
        ) / total,
        2
    )

    avg_completeness = round(
        sum(
            row["Completeness"]
            for row in results
        ) / total,
        2
    )

    avg_overall = round(
        sum(
            row["Overall"]
            for row in results
        ) / total,
        2
    )

    # =====================================
    # Summary
    # =====================================

    story.append(
        Paragraph(
            "<b>Batch Summary</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Total Evaluations : {total}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"PASS : {pass_count}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Needs Improvement : {needs_count}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"FAIL : {fail_count}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "<b>Average Scores</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"Relevance : {avg_relevance}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Accuracy : {avg_accuracy}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Hallucination : {avg_hallucination}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Completeness : {avg_completeness}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Overall : {avg_overall}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))
        # =====================================
    # Individual Evaluation Results
    # =====================================

    story.append(
        Paragraph(
            "<b>Individual Evaluation Results</b>",
            styles["Heading2"]
        )
    )

    table_data = [

        [
            "Question",
            "Overall",
            "Verdict"
        ]

    ]

    for row in results:

        question = row["Question"]

        if len(question) > 60:
            question = question[:60] + "..."

        table_data.append(

            [
                question,
                str(row["Overall"]),
                row["Verdict"]
            ]

        )

    table = Table(
        table_data,
        colWidths=[
            4.2 * inch,
            1.0 * inch,
            1.5 * inch
        ]
    )

    table.setStyle(

        TableStyle(

            [

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.darkblue
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.white
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.black
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),

                (
                    "ALIGN",
                    (0, 0),
                    (-1, -1),
                    "CENTER"
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, 0),
                    10
                ),

                (
                    "BACKGROUND",
                    (0, 1),
                    (-1, -1),
                    colors.beige
                )

            ]

        )

    )

    story.append(table)

    story.append(Spacer(1, 20))

    # =====================================
    # Flagged Responses
    # =====================================

    story.append(

        Paragraph(

            "<b>Flagged Responses</b>",

            styles["Heading2"]

        )

    )

    flagged = [

        row

        for row in results

        if row["Verdict"] != "PASS"

    ]

    if len(flagged) == 0:

        story.append(

            Paragraph(

                "No flagged responses detected.",

                styles["BodyText"]

            )

        )

    else:

        for index, row in enumerate(flagged, start=1):

            story.append(

                Paragraph(

                    f"<b>{index}.</b> {row['Question']}",

                    styles["BodyText"]

                )

            )

            story.append(

                Paragraph(

                    f"Verdict : {row['Verdict']}",

                    styles["BodyText"]

                )

            )

            story.append(

                Paragraph(

                    f"Overall Score : {row['Overall']}",

                    styles["BodyText"]

                )

            )

            story.append(

                Spacer(1, 8)

            )

    story.append(

        Spacer(1, 20)

    )
        # =====================================
    # Improvement Recommendations
    # =====================================

    story.append(
        Paragraph(
            "<b>Improvement Recommendations</b>",
            styles["Heading2"]
        )
    )

    recommendations = []

    if avg_relevance < 0.80:
        recommendations.append(
            "• Improve response relevance by ensuring answers directly address the user's question."
        )

    if avg_accuracy < 0.80:
        recommendations.append(
            "• Improve factual accuracy by grounding responses with reliable reference information."
        )

    if avg_hallucination < 0.90:
        recommendations.append(
            "• Reduce hallucinations by strengthening Retrieval-Augmented Generation (RAG) context."
        )

    if avg_completeness < 0.80:
        recommendations.append(
            "• Improve completeness by covering all important aspects of the question."
        )

    if avg_overall < 0.80:
        recommendations.append(
            "• Overall evaluation quality can be improved by refining AI prompts and knowledge sources."
        )

    if len(recommendations) == 0:

        story.append(
            Paragraph(
                "Excellent performance. No major improvements are recommended.",
                styles["BodyText"]
            )
        )

    else:

        for rec in recommendations:

            story.append(
                Paragraph(
                    rec,
                    styles["BodyText"]
                )
            )

    story.append(
        Spacer(1, 20)
    )

    # =====================================
    # Final Summary
    # =====================================

    story.append(
        Paragraph(
            "<b>Conclusion</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"""
This batch evaluation processed <b>{total}</b> AI-generated responses.

Average Overall Score: <b>{avg_overall}</b><br/>

PASS: <b>{pass_count}</b><br/>

Needs Improvement: <b>{needs_count}</b><br/>

FAIL: <b>{fail_count}</b><br/><br/>

The report summarizes evaluation performance across Relevance,
Accuracy, Hallucination Detection, and Completeness using the
multi-agent evaluation framework.
""",
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            "<i>Generated by AI Evaluation Platform - Milestone 4</i>",
            styles["Italic"]
        )
    )

    # =====================================
    # Build PDF
    # =====================================

    pdf.build(story)

    return filename