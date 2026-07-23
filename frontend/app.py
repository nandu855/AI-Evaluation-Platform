import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Evaluation Platform",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Evaluation Platform")
st.markdown(
    """
Evaluate AI-generated responses using a Retrieval-Augmented Generation (RAG)
pipeline and multiple AI Judge Agents.
"""
)

tab1, tab2 = st.tabs(
    [
        "📝 Single Evaluation",
        "📂 Batch Evaluation"
    ]
)

# =====================================================
# SINGLE EVALUATION
# =====================================================

with tab1:

    st.header("Single Response Evaluation")

    question = st.text_area(
        "Question",
        height=100,
        placeholder="Enter the question..."
    )

    ai_answer = st.text_area(
        "AI Generated Answer",
        height=180,
        placeholder="Paste AI generated answer..."
    )

    reference_answer = st.text_area(
        "Reference Answer (Optional)",
        height=180,
        placeholder="Reference answer..."
    )

    if st.button(
        "🚀 Evaluate",
        use_container_width=True
    ):

        if not question.strip():

            st.error("Question is required.")
            st.stop()

        if not ai_answer.strip():

            st.error("AI response is required.")
            st.stop()

        payload = {

            "question": question,

            "ai_response": ai_answer,

            "reference_answer": reference_answer

        }

        with st.spinner("Evaluating..."):

            try:

                response = requests.post(

                    f"{API_URL}/evaluate",

                    json=payload,

                    timeout=300

                )

                response.raise_for_status()

                result = response.json()

            except Exception as e:

                st.error(f"Backend Error:\n\n{e}")

                st.stop()

        st.success("Evaluation Completed Successfully!")

        judge = result["judge_results"]

        overall = judge["overall_score"]

        verdict = judge["verdict"]

        summary = judge["summary"]

        # ==========================================
        # Dashboard
        # ==========================================

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(

                "Overall Score",

                f"{overall:.2f}"

            )

            st.progress(overall)

        with col2:

            if verdict == "PASS":

                st.success(verdict)

            elif verdict == "Needs Improvement":

                st.warning(verdict)

            else:

                st.error(verdict)

        with col3:

            st.info(summary)

        st.divider()

        # ==========================================
        # Dimension Scores
        # ==========================================

        st.subheader("Evaluation Dimensions")

        d1, d2 = st.columns(2)

        with d1:

            st.metric(

                "Relevance",

                f"{judge['relevance']['score']:.2f}"

            )

            st.progress(

                judge["relevance"]["score"]

            )

            st.metric(

                "Accuracy",

                f"{judge['accuracy']['score']:.2f}"

            )

            st.progress(

                judge["accuracy"]["score"]

            )

        with d2:

            st.metric(

                "Hallucination",

                f"{judge['hallucination']['score']:.2f}"

            )

            st.progress(

                judge["hallucination"]["score"]

            )

            st.metric(

                "Completeness",

                f"{judge['completeness']['score']:.2f}"

            )

            st.progress(

                judge["completeness"]["score"]

            )

        st.divider()

        # ==========================================
        # Retrieved Context
        # ==========================================

        with st.expander(
            "📚 Retrieved Context",
            expanded=False
        ):

            st.write(
                result["retrieved_context"]
            )

        st.divider()

        # ==========================================
        # Judge Agents
        # ==========================================

        st.header("Judge Agent Analysis")

        # ----------------------------
        # Relevance Judge
        # ----------------------------

        with st.container():

            st.subheader("🟢 Relevance Judge")

            st.metric(

                "Score",

                f"{judge['relevance']['score']:.2f}"

            )

            st.write("Reason")

            st.info(

                judge["relevance"]["reason"]

            )

        st.divider()

        # ----------------------------
        # Accuracy Judge
        # ----------------------------

        with st.container():

            st.subheader("🔵 Accuracy Judge")

            st.metric(

                "Score",

                f"{judge['accuracy']['score']:.2f}"

            )

            st.write("Reason")

            st.info(

                judge["accuracy"]["reason"]

            )

            st.write("Evidence")

            st.success(

                judge["accuracy"]["evidence"]

            )

        st.divider()
                # ----------------------------
        # Hallucination Judge
        # ----------------------------

        with st.container():

            st.subheader("🟠 Hallucination Judge")

            st.metric(
                "Score",
                f"{judge['hallucination']['score']:.2f}"
            )

            st.write("Reason")

            st.info(
                judge["hallucination"]["reason"]
            )

            st.write("Unsupported Claims")

            claims = judge["hallucination"]["unsupported_claims"]

            if claims:

                for claim in claims:
                    st.error(claim)

            else:

                st.success("No unsupported claims detected.")

        st.divider()

        # ----------------------------
        # Completeness Judge
        # ----------------------------

        with st.container():

            st.subheader("🟣 Completeness Judge")

            st.metric(
                "Score",
                f"{judge['completeness']['score']:.2f}"
            )

            st.write("Reason")

            st.info(
                judge["completeness"]["reason"]
            )

            st.write("Covered Points")

            covered = judge["completeness"]["covered"]

            if covered:
                for item in covered:
                    st.success(item)
            else:
                st.info("No covered points reported.")

            st.write("Missing Points")

            missing = judge["completeness"]["missing"]

            if missing:
                for item in missing:
                    st.warning(item)
            else:
                st.success("Nothing important is missing.")

        st.divider()

        # ==========================================
        # Final Verdict
        # ==========================================

        st.header("Final Verdict")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Overall Score",
                f"{judge['overall_score']:.2f}"
            )

            st.progress(judge["overall_score"])

        with col2:

            verdict = judge["verdict"]

            if verdict == "PASS":
                st.success(verdict)

            elif verdict == "Needs Improvement":
                st.warning(verdict)

            else:
                st.error(verdict)

            st.write("Summary")

            st.info(judge["summary"])

        st.divider()

        # ==========================================
        # LLM Judge
        # ==========================================

        st.header("🧠 LLM Judge Report")

        st.markdown(judge["llm_reasoning"])

        st.divider()

        # ==========================================
        # Score Table
        # ==========================================

        st.header("Evaluation Summary")

        df = pd.DataFrame(
            {
                "Metric": [
                    "Relevance",
                    "Accuracy",
                    "Hallucination",
                    "Completeness",
                    "Overall"
                ],
                "Score": [
                    judge["relevance"]["score"],
                    judge["accuracy"]["score"],
                    judge["hallucination"]["score"],
                    judge["completeness"]["score"],
                    judge["overall_score"]
                ]
            }
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            "⬇ Download JSON Report",
            data=response.text,
            file_name="evaluation_report.json",
            mime="application/json",
            use_container_width=True
        )

# =====================================================
# BATCH EVALUATION
# =====================================================

with tab2:

    st.header("Batch Evaluation")

    st.markdown(
        """
Upload a CSV containing the following columns:

- question
- ai_response
- reference_answer
"""
    )

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:

            df = pd.read_csv(uploaded_file)

            st.subheader("Preview")

            st.dataframe(
                df.head(),
                use_container_width=True
            )

            required_columns = [
                "question",
                "ai_response",
                "reference_answer"
            ]

            missing_columns = [
                col for col in required_columns
                if col not in df.columns
            ]

            if missing_columns:

                st.error(
                    f"Missing required columns: {', '.join(missing_columns)}"
                )

            elif st.button(
                "🚀 Run Batch Evaluation",
                use_container_width=True
            ):

                results = []

                progress = st.progress(0)

                total = len(df)

                for index, row in df.iterrows():

                    payload = {
                        "question": row["question"],
                        "ai_response": row["ai_response"],
                        "reference_answer": row["reference_answer"]
                    }

                    try:

                        response = requests.post(
                            f"{API_URL}/evaluate",
                            json=payload,
                            timeout=300
                        )

                        response.raise_for_status()

                        result = response.json()

                        judge = result["judge_results"]

                        results.append(
                            {
                                "Question": row["question"],
                                "Overall": judge["overall_score"],
                                "Verdict": judge["verdict"],
                                "Relevance": judge["relevance"]["score"],
                                "Accuracy": judge["accuracy"]["score"],
                                "Hallucination": judge["hallucination"]["score"],
                                "Completeness": judge["completeness"]["score"]
                            }
                        )

                    except Exception:

                        results.append(
                            {
                                "Question": row["question"],
                                "Overall": 0,
                                "Verdict": "ERROR",
                                "Relevance": 0,
                                "Accuracy": 0,
                                "Hallucination": 0,
                                "Completeness": 0
                            }
                        )

                    progress.progress((index + 1) / total)

                result_df = pd.DataFrame(results)

                st.success("Batch Evaluation Completed")

                st.dataframe(
                    result_df,
                    use_container_width=True
                )

                st.subheader("Statistics")

                c1, c2, c3 = st.columns(3)

                with c1:
                    st.metric(
                        "Average Overall",
                        f"{result_df['Overall'].mean():.2f}"
                    )

                with c2:
                    st.metric(
                        "PASS",
                        int((result_df["Verdict"] == "PASS").sum())
                    )

                with c3:
                    st.metric(
                        "FAIL",
                        int((result_df["Verdict"] == "FAIL").sum())
                    )

                csv = result_df.to_csv(index=False).encode("utf-8")

                st.download_button(
                    "⬇ Download Batch Results",
                    csv,
                    "batch_results.csv",
                    "text/csv",
                    use_container_width=True
                )

        except Exception as e:

            st.error(str(e))