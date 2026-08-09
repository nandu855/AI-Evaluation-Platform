import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def show_dashboard(result_df: pd.DataFrame):

    st.divider()

    st.title("📊 Evaluation Scoring Dashboard")

    # ----------------------------------------
    # Basic Statistics
    # ----------------------------------------

    total = len(result_df)

    pass_count = (
        result_df["Verdict"] == "PASS"
    ).sum()

    needs_count = (
        result_df["Verdict"] == "Needs Improvement"
    ).sum()

    fail_count = (
        result_df["Verdict"] == "FAIL"
    ).sum()

    avg_relevance = result_df["Relevance"].mean()

    avg_accuracy = result_df["Accuracy"].mean()

    avg_hallucination = result_df["Hallucination"].mean()

    avg_completeness = result_df["Completeness"].mean()

    avg_overall = result_df["Overall"].mean()

    hallucination_frequency = (
        result_df["Hallucination"] < 0.80
    ).sum()

    # ----------------------------------------
    # KPI Cards
    # ----------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Total Evaluations",
            total
        )

    with c2:
        st.metric(
            "PASS",
            int(pass_count)
        )

    with c3:
        st.metric(
            "Needs Improvement",
            int(needs_count)
        )

    with c4:
        st.metric(
            "FAIL",
            int(fail_count)
        )

    st.divider()

    # ----------------------------------------
    # Average Scores
    # ----------------------------------------

    st.subheader("Average Dimension Scores")

    a1, a2, a3, a4, a5 = st.columns(5)

    with a1:
        st.metric(
            "Relevance",
            f"{avg_relevance:.2f}"
        )

    with a2:
        st.metric(
            "Accuracy",
            f"{avg_accuracy:.2f}"
        )

    with a3:
        st.metric(
            "Hallucination",
            f"{avg_hallucination:.2f}"
        )

    with a4:
        st.metric(
            "Completeness",
            f"{avg_completeness:.2f}"
        )

    with a5:
        st.metric(
            "Overall",
            f"{avg_overall:.2f}"
        )

    st.divider()

    st.subheader("Hallucination Frequency")

    st.metric(
        "Flagged Responses",
        hallucination_frequency
    )

    st.divider()
        # ==========================================
    # Bar Chart
    # ==========================================

    st.subheader("📊 Average Score Comparison")

    score_df = pd.DataFrame(
        {
            "Metric": [
                "Relevance",
                "Accuracy",
                "Hallucination",
                "Completeness",
                "Overall"
            ],
            "Average Score": [
                avg_relevance,
                avg_accuracy,
                avg_hallucination,
                avg_completeness,
                avg_overall
            ]
        }
    )

    st.bar_chart(
        score_df.set_index("Metric")
    )

    st.divider()

    # ==========================================
    # Pie Chart
    # ==========================================

    st.subheader("🥧 Verdict Distribution")

    fig1, ax1 = plt.subplots(figsize=(5, 5))

    labels = [
        "PASS",
        "Needs Improvement",
        "FAIL"
    ]

    values = [
        pass_count,
        needs_count,
        fail_count
    ]

    ax1.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    ax1.axis("equal")

    st.pyplot(fig1)

    st.divider()

    # ==========================================
    # Overall Score Trend
    # ==========================================

    st.subheader("📈 Overall Score Trend")

    trend_df = result_df.copy()

    trend_df["Evaluation"] = range(
        1,
        len(trend_df) + 1
    )

    trend_df = trend_df.set_index(
        "Evaluation"
    )

    st.line_chart(
        trend_df["Overall"]
    )

    st.divider()

    # ==========================================
    # Dimension Trend
    # ==========================================

    st.subheader("📈 Dimension Trends")

    dimension_df = result_df[
        [
            "Relevance",
            "Accuracy",
            "Hallucination",
            "Completeness"
        ]
    ]

    st.line_chart(
        dimension_df
    )

    st.divider()
        # ==========================================
    # Flagged Responses
    # ==========================================

    st.subheader("🚩 Flagged Responses")

    flagged = result_df[
        (result_df["Verdict"] != "PASS") |
        (result_df["Hallucination"] < 0.80)
    ]

    if len(flagged) == 0:

        st.success(
            "No problematic responses detected."
        )

    else:

        st.dataframe(
            flagged,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    # ==========================================
    # Filters
    # ==========================================

    st.subheader("🔍 Filter Results")

    verdict_filter = st.selectbox(
        "Select Verdict",
        [
            "All",
            "PASS",
            "Needs Improvement",
            "FAIL"
        ]
    )

    if verdict_filter == "All":

        filtered_df = result_df

    else:

        filtered_df = result_df[
            result_df["Verdict"] == verdict_filter
        ]

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ==========================================
    # Download Results
    # ==========================================

    csv = filtered_df.to_csv(
        index=False
    )

    st.download_button(

        "⬇ Download Dashboard Results",

        data=csv,

        file_name="dashboard_results.csv",

        mime="text/csv",

        use_container_width=True

    )

    st.divider()

    # ==========================================
    # Dashboard Summary
    # ==========================================

    st.success(
        f"""
Dashboard Summary

• Total Evaluations : {total}

• PASS : {pass_count}

• Needs Improvement : {needs_count}

• FAIL : {fail_count}

• Average Overall Score : {avg_overall:.2f}

• Hallucination Frequency : {hallucination_frequency}
"""
    )