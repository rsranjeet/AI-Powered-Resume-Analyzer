import streamlit as st
from resume_parser import extract_skills, score_resume, extract_text

st.title("🧠 AI-Powered Resume Analyzer")

# Upload files
resume_file = st.file_uploader("Upload Resume (.TXT, .PDF, .DOCX)", type=["txt", "pdf", "docx"])
job_file = st.file_uploader("Upload Job Description (.TXT, .PDF, .DOCX)", type=["txt", "pdf", "docx"])

# Process files when both are uploaded
if resume_file and job_file:
    # Determine file extensions
    resume_ext = resume_file.name.split(".")[-1].lower()
    job_ext = job_file.name.split(".")[-1].lower()

    # Extract text
    resume_text = extract_text(resume_file, resume_ext)
    job_text = extract_text(job_file, job_ext)

    # Extract skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    # Display raw text
    st.subheader("Raw Resume Text")
    st.code(resume_text, language='text')

    st.subheader("Raw Job Description Text")
    st.code(job_text, language='text')

    # Display extracted skills
    st.subheader("Extracted Skills")
    st.write("**Resume Skills:**", resume_skills)
    st.write("**Job Requirements:**", job_skills)

    # Score and show result
    score = score_resume(resume_skills, job_skills)
    st.subheader(f"🎯 Resume Match Score: {score}%")
