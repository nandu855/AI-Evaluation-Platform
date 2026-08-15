from html import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


# ============================================================
# SAFE TEXT HELPERS
# ============================================================

def safe_text(value):
    """
    Convert strings, dictionaries, lists and other values
    into safe ReportLab HTML text.
    """

    if value is None:
        return ""

    if isinstance(value, str):
        return escape(value).replace("\n", "<br/>")

    if isinstance(value, (int, float, bool)):
        return escape(str(value))

    if isinstance(value, dict):
        parts = []

        for key, item in value.items():
            parts.append(
                f"<b>{escape(str(key))}:</b> {safe_text(item)}"
            )

        return "<br/>".join(parts)

    if isinstance(value, list):
        parts = []

        for item in value:
            parts.append(
                f"• {safe_text(item)}"
            )

        return "<br/>".join(parts)

    return escape(str(value))


def list_to_text(value):
    """
    Safely convert a list containing strings or dictionaries
    into readable report text.
    """

    if value is None:
        return "None"

    if not isinstance(value, list):
        return safe_text(value)

    if len(value) == 0:
        return "None"

    result = []

    for item in value:
        result.append(
            f"• {safe_text(item)}"
        )

    return "<br/>".join(result)


# ============================================================
# SECTION TITLE
# ============================================================

def add_section_title(story, title, section_style):
    """
    Add a section heading using the explicitly supplied style.
    """

    story.append(
        Spacer(1, 8)
    )

    story.append(
        Paragraph(
            f"<b>{escape(title)}</b>",
            section_style
        )
    )

    story.append(
        Spacer(1, 6)
    )


# ============================================================
# LABEL + VALUE
# ============================================================

def add_label_value(
    story,
    label,
    value,
    body_style
):
    """
    Add a formatted label and value.
    """

    story.append(
        Paragraph(
            f"<b>{escape(label)}:</b> {safe_text(value)}",
            body_style
        )
    )

    story.append(
        Spacer(1, 5)
    )


# ============================================================
# MAIN REPORT FUNCTION
# ============================================================

def generate_report(
    filename,
    question,
    ai_answer,
    reference_answer,
    retrieved_context,
    judge_results
):

    # ========================================================
    # BASE STYLES
    # ========================================================

    base_styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CustomTitle",
        parent=base_styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#17365D"),
        spaceAfter=14,
    )

    subtitle_style = ParagraphStyle(
        "CustomSubtitle",
        parent=base_styles["BodyText"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#555555"),
        spaceAfter=10,
    )

    section_style = ParagraphStyle(
        "CustomSectionHeading",
        parent=base_styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#17365D"),
        spaceBefore=8,
        spaceAfter=6,
    )

    body_style = ParagraphStyle(
        "CustomBody",
        parent=base_styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=14,
        textColor=colors.black,
        spaceAfter=4,
    )

    small_style = ParagraphStyle(
        "CustomSmall",
        parent=base_styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=12,
        textColor=colors.black,
    )

    score_style = ParagraphStyle(
        "CustomScore",
        parent=base_styles["BodyText"],
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#17365D"),
    )

    # ========================================================
    # PDF DOCUMENT
    # ========================================================

    pdf = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm,
        title="AI Response Validation Report",
        author="AI Response Validation System",
    )

    story = []

    # ========================================================
    # TITLE
    # ========================================================

    story.append(
        Paragraph(
            "AI RESPONSE VALIDATION REPORT",
            title_style
        )
    )

    story.append(
        Paragraph(
            "Development of AI Response Validation System "
            "with Hallucination Detection Assistance",
            subtitle_style
        )
    )

    story.append(
        Spacer(1, 10)
    )

    # ========================================================
    # SECTION 1
    # ========================================================

    add_section_title(
        story,
        "1. Evaluation Input",
        section_style
    )

    add_label_value(
        story,
        "Question",
        question,
        body_style
    )

    add_label_value(
        story,
        "AI Generated Answer",
        ai_answer,
        body_style
    )

    add_label_value(
        story,
        "Reference Answer",
        reference_answer,
        body_style
    )

    # ========================================================
    # SECTION 2
    # ========================================================

    add_section_title(
        story,
        "2. Retrieved Context",
        section_style
    )

    if retrieved_context:
        story.append(
            Paragraph(
                safe_text(retrieved_context),
                body_style
            )
        )
    else:
        story.append(
            Paragraph(
                "No retrieved context available.",
                body_style
            )
        )

    story.append(
        Spacer(1, 10)
    )

    # ========================================================
    # SECTION 3
    # ========================================================

    add_section_title(
        story,
        "3. Judge Agent Results",
        section_style
    )

    # --------------------------------------------------------
    # RELEVANCE
    # --------------------------------------------------------

    relevance = judge_results.get(
        "relevance",
        {}
    )

    story.append(
        Paragraph(
            "<b>Relevance Evaluation</b>",
            score_style
        )
    )

    add_label_value(
        story,
        "Score",
        relevance.get("score", "N/A"),
        body_style
    )

    add_label_value(
        story,
        "Reason",
        relevance.get("reason", "N/A"),
        body_style
    )

    # --------------------------------------------------------
    # ACCURACY
    # --------------------------------------------------------

    accuracy = judge_results.get(
        "accuracy",
        {}
    )

    story.append(
        Spacer(1, 8)
    )

    story.append(
        Paragraph(
            "<b>Accuracy Evaluation</b>",
            score_style
        )
    )

    add_label_value(
        story,
        "Score",
        accuracy.get("score", "N/A"),
        body_style
    )

    add_label_value(
        story,
        "Reason",
        accuracy.get("reason", "N/A"),
        body_style
    )

    add_label_value(
        story,
        "Evidence",
        accuracy.get("evidence", "N/A"),
        body_style
    )

    # --------------------------------------------------------
    # HALLUCINATION
    # --------------------------------------------------------

    hallucination = judge_results.get(
        "hallucination",
        {}
    )

    story.append(
        Spacer(1, 8)
    )

    story.append(
        Paragraph(
            "<b>Hallucination Detection Assistance</b>",
            score_style
        )
    )

    add_label_value(
        story,
        "Score",
        hallucination.get("score", "N/A"),
        body_style
    )

    add_label_value(
        story,
        "Reason",
        hallucination.get("reason", "N/A"),
        body_style
    )

    story.append(
        Paragraph(
            "<b>Unsupported Claims:</b>",
            body_style
        )
    )

    story.append(
        Paragraph(
            list_to_text(
                hallucination.get(
                    "unsupported_claims",
                    []
                )
            ),
            small_style
        )
    )

    # --------------------------------------------------------
    # COMPLETENESS
    # --------------------------------------------------------

    completeness = judge_results.get(
        "completeness",
        {}
    )

    story.append(
        Spacer(1, 8)
    )

    story.append(
        Paragraph(
            "<b>Completeness Evaluation</b>",
            score_style
        )
    )

    add_label_value(
        story,
        "Score",
        completeness.get("score", "N/A"),
        body_style
    )

    story.append(
        Paragraph(
            "<b>Covered:</b>",
            body_style
        )
    )

    story.append(
        Paragraph(
            list_to_text(
                completeness.get(
                    "covered",
                    []
                )
            ),
            small_style
        )
    )

    story.append(
        Spacer(1, 4)
    )

    story.append(
        Paragraph(
            "<b>Missing:</b>",
            body_style
        )
    )

    story.append(
        Paragraph(
            list_to_text(
                completeness.get(
                    "missing",
                    []
                )
            ),
            small_style
        )
    )

    story.append(
        Spacer(1, 4)
    )

    add_label_value(
        story,
        "Reason",
        completeness.get(
            "reason",
            "N/A"
        ),
        body_style
    )

    # ========================================================
    # SECTION 4
    # ========================================================

    add_section_title(
        story,
        "4. Final Evaluation",
        section_style
    )

    overall_score = judge_results.get(
        "overall_score",
        "N/A"
    )

    verdict = judge_results.get(
        "verdict",
        "N/A"
    )

    summary = judge_results.get(
        "summary",
        "N/A"
    )

    score_data = [
        [
            Paragraph(
                "<b>Overall Score</b>",
                body_style
            ),
            Paragraph(
                safe_text(overall_score),
                body_style
            ),
        ],
        [
            Paragraph(
                "<b>Verdict</b>",
                body_style
            ),
            Paragraph(
                safe_text(verdict),
                body_style
            ),
        ],
    ]

    score_table = Table(
        score_data,
        colWidths=[
            45 * mm,
            120 * mm,
        ]
    )

    score_table.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (0, -1),
                    colors.HexColor("#EAF1F8"),
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.HexColor("#B8C7D9"),
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP",
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    7,
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    6,
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    6,
                ),
            ]
        )
    )

    story.append(
        score_table
    )

    story.append(
        Spacer(1, 10)
    )

    add_label_value(
        story,
        "Summary",
        summary,
        body_style
    )

    # ========================================================
    # SECTION 5
    # ========================================================

    add_section_title(
        story,
        "5. LLM Evaluation Explanation",
        section_style
    )

    llm_reasoning = judge_results.get(
        "llm_reasoning",
        "No LLM reasoning available."
    )

    story.append(
        Paragraph(
            safe_text(llm_reasoning),
            body_style
        )
    )

    # ========================================================
    # PROJECT INFORMATION
    # ========================================================

    add_section_title(
        story,
        "6. Project Information",
        section_style
    )

    add_label_value(
        story,
        "Project Title",
        "Development of AI Response Validation System "
        "with Hallucination Detection Assistance",
        body_style
    )

    add_label_value(
        story,
        "Presenter",
        "BADARALA ANAND KUMAR",
        body_style
    )

    add_label_value(
        story,
        "Email",
        "anand.badarala@gmail.com",
        body_style
    )

    add_label_value(
        story,
        "Mobile",
        "9441148377",
        body_style
    )

    # ========================================================
    # BUILD PDF
    # ========================================================

    pdf.build(story)

    return filename