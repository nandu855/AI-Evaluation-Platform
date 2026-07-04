import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="AI Evaluation Platform",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Evaluation Platform")
st.markdown("Evaluate AI-generated answers using Retrieval-Augmented Generation (RAG).")

st.divider()

# -------------------------
# Input Section
# -------------------------

question = st.text_area(
    "Question",
    height=100,
    placeholder="Enter your question..."
)

ai_answer = st.text_area(
    "AI Generated Answer",
    height=150,
    placeholder="Paste the AI generated answer..."
)

reference_answer = st.text_area(
    "Reference Answer (Optional)",
    height=150,
    placeholder="Reference answer..."
)

st.divider()

if st.button("🚀 Evaluate Answer", use_container_width=True):

    if question.strip() == "" or ai_answer.strip() == "":
        st.error("Question and AI Answer are required.")
        st.stop()

    payload = {
        "question": question,
        "ai_response": ai_answer,
        "reference_answer": reference_answer
    }

    with st.spinner("Evaluating..."):

        try:

            response = requests.post(
                "http://127.0.0.1:8000/evaluate",
                json=payload,
                timeout=120
            )

            if response.status_code != 200:
                st.error(f"Backend Error ({response.status_code})")
                st.code(response.text)
                st.stop()

            result = response.json()

        except Exception as e:
            st.error(f"Cannot connect to backend.\n\n{e}")
            st.stop()

    st.success("Evaluation Completed Successfully!")

    st.divider()

    overall = float(result["overall_score"])

    if overall >= 0.75:
        verdict_color = "🟢"
    elif overall >= 0.50:
        verdict_color = "🟡"
    else:
        verdict_color = "🔴"

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Overall Score",
            f"{overall:.2f}"
        )

        st.progress(overall)

        st.subheader(f"{verdict_color} {result['verdict']}")

    with col2:

        st.metric(
            "Relevance",
            f"{result['relevance_score']:.2f}"
        )
        st.progress(float(result["relevance_score"]))

        st.metric(
            "Accuracy",
            f"{result['accuracy_score']:.2f}"
        )
        st.progress(float(result["accuracy_score"]))

        st.metric(
            "Hallucination",
            f"{result['hallucination_score']:.2f}"
        )
        st.progress(float(result["hallucination_score"]))

        st.metric(
            "Completeness",
            f"{result['completeness_score']:.2f}"
        )
        st.progress(float(result["completeness_score"]))

    st.divider()

    with st.expander("📚 Retrieved Context", expanded=False):

        st.write(result["retrieved_context"])

    st.divider()

    st.subheader("Evaluation Summary")

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
                result["relevance_score"],
                result["accuracy_score"],
                result["hallucination_score"],
                result["completeness_score"],
                result["overall_score"]
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