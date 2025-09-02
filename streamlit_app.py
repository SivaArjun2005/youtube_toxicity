
import streamlit as st
from utils.classifier import predict_toxicity

st.title("💬 YouTube Comment Toxicity Analyzer")

comment = st.text_area("Paste a YouTube Comment Below:")

if st.button("Analyze"):
    if comment.strip() == "":
        st.warning("Please enter a comment to analyze.")
    else:
        result = predict_toxicity(comment)
        if result == "Toxic":
            st.error("🚫 This comment is likely TOXIC.")
        else:
            st.success("✅ This comment seems NON-TOXIC.")
