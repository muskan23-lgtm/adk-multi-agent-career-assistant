from pathlib import Path
import sys
import tempfile

import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
load_dotenv(PROJECT_ROOT / ".env")

from utils.resume_parser import parse_resume
from utils.ats_scorer import score_resume_job
from utils.skill_extractor import identify_skill_gaps
from utils.report_generator import create_pdf_report

st.set_page_config(page_title="AI Career Assistant", page_icon="🧭", layout="wide")
st.title("🧭 AI-Powered Career Assistant")
st.caption("Resume intelligence • Explainable job matching • Skill-gap analysis • Career planning")

with st.sidebar:
    st.header("How it works")
    st.write("1. Add your resume")
    st.write("2. Paste a target job description")
    st.write("3. Review match evidence and skill gaps")
    st.info("Your resume is processed in this app session and is not saved by this starter project.")

left, right = st.columns(2)
with left:
    st.subheader("1. Resume")
    uploaded = st.file_uploader("Upload PDF, DOCX or TXT", type=["pdf", "docx", "txt"])
    resume_text = st.text_area("Or paste resume text", height=260, placeholder="Paste your resume here...")
    if uploaded is not None:
        suffix = Path(uploaded.name).suffix.lower()
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded.getvalue())
            temp_path = tmp.name
        try:
            parsed = parse_resume(temp_path)
            if parsed.strip():
                resume_text = parsed
                st.success(f"Extracted text from {uploaded.name}")
            else:
                st.warning("No selectable text found. Scanned PDFs may require OCR.")
        finally:
            Path(temp_path).unlink(missing_ok=True)

with right:
    st.subheader("2. Target job")
    role_title = st.text_input("Target role", placeholder="e.g. Data Analyst Intern")
    job_text = st.text_area("Paste job description", height=320, placeholder="Paste responsibilities and requirements...")

if st.button("Analyze career fit", type="primary", use_container_width=True):
    if not resume_text.strip() or not job_text.strip():
        st.error("Please provide both resume text and a job description.")
    else:
        result = score_resume_job(resume_text, job_text)
        st.session_state["analysis_result"] = result
        st.session_state["role_title"] = role_title or "Target role"

result = st.session_state.get("analysis_result")
if result:
    st.divider()
    st.subheader("3. Career fit results")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Estimated match", f"{result['score']}%")
    c2.metric("Skill coverage", f"{result['skill_coverage']}%")
    c3.metric("Keyword coverage", f"{result['keyword_coverage']}%")
    c4.metric("Experience signals", f"{result['experience_signal_coverage']}%")
    st.caption(result["note"])

    chart_df = pd.DataFrame({
        "Metric": ["Skills", "Keywords", "Experience signals"],
        "Coverage (%)": [result["skill_coverage"], result["keyword_coverage"], result["experience_signal_coverage"]]
    })
    st.plotly_chart(px.bar(chart_df, x="Metric", y="Coverage (%)", range_y=[0, 100],
                           title="Evidence coverage breakdown"), use_container_width=True)

    a, b = st.columns(2)
    with a:
        st.markdown("#### ✅ Matched skills")
        if result["matched_skills"]:
            for skill in result["matched_skills"]:
                st.write(f"- {skill}")
        else:
            st.write("No taxonomy matches detected.")
    with b:
        st.markdown("#### 🎯 Skills not demonstrated")
        if result["not_demonstrated_skills"]:
            for skill in result["not_demonstrated_skills"]:
                st.write(f"- {skill}")
        else:
            st.write("No gaps detected in the current taxonomy.")

    st.markdown("#### 📚 Suggested 30-day action plan")
    gaps = result["not_demonstrated_skills"]
    if gaps:
        for i, skill in enumerate(gaps[:6], start=1):
            st.write(f"**Week {((i-1)//2)+1}:** Learn and practice **{skill}**; build a small project or add a truthful example demonstrating it.")
    else:
        st.write("Strengthen your portfolio with one end-to-end project aligned to the target role.")
    st.markdown("#### 🧩 Resume skills detected")
    st.write(", ".join(result["resume_skills"]) or "No skills from the included taxonomy detected.")

    pdf_bytes = create_pdf_report(result, st.session_state.get("role_title", "Target role"))
    st.download_button("⬇️ Download career analysis PDF", data=pdf_bytes,
                       file_name="career_fit_report.pdf", mime="application/pdf")
