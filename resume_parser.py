import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Example skill keywords (extend this list)
SKILL_KEYWORDS = {
    "python", "java", "react", "sql", "machine learning",
    "data analysis", "django", "node.js", "nlp", "flask",
    "git", "html", "css", "javascript"
}

def extract_skills(text):
    doc = nlp(text.lower())
    extracted_skills = set()
    for token in doc:
        if token.text in SKILL_KEYWORDS:
            extracted_skills.add(token.text)
    return list(extracted_skills)

def score_resume(resume_skills, job_skills):
    if not job_skills:
        return 0
    matched = set(resume_skills).intersection(set(job_skills))
    return int(len(matched) / len(job_skills) * 100)
