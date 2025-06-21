import streamlit as st
from resume_parser import extract_skills, score_resume

st.title("🧠 AI-Powered Resume Analyzer")

# Upload resume and job description
resume_file = st.file_uploader("Upload Resume (TXT)", type="txt")
job_file = st.file_uploader("Upload Job Description (TXT)", type="txt")

if resume_file and job_file:
    resume_text = resume_file.read().decode("utf-8")
    job_text = job_file.read().decode("utf-8")

    st.subheader("Extracted Skills")
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    st.write("**Resume Skills:**", resume_skills)
    st.write("**Job Requirements:**", job_skills)

    # Score
    score = score_resume(resume_skills, job_skills)
    st.subheader(f"Resume Match Score: {score}%")
