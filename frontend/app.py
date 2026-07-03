import streamlit as st

st.title("AI Evaluation Platform")

question = st.text_area("Question")

answer = st.text_area("AI Answer")

reference = st.text_area("Reference Answer")

if st.button("Submit"):
    st.success("Data Submitted")
    