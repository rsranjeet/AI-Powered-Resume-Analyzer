import spacy
from docx import Document
import PyPDF2
import io

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define common skill keywords
SKILL_KEYWORDS = {
    "python", "java", "react", "sql", "machine learning",
    "data analysis", "django", "node.js", "nlp", "flask",
    "git", "html", "css", "javascript"
}


def extract_text(file, file_type):
    if file_type == "txt":
        return file.read().decode("utf-8")

    elif file_type == "pdf":
        reader = PyPDF2.PdfReader(file)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    elif file_type == "docx":
        doc = Document(io.BytesIO(file.read()))
        return "\n".join([para.text for para in doc.paragraphs])

    return ""


# def extract_skills(text):
#     doc = nlp(text.lower())
#     return list({token.text for token in doc if token.text in SKILL_KEYWORDS})

from spacy.matcher import PhraseMatcher

def extract_skills(text):
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp.make_doc(skill) for skill in SKILL_KEYWORDS]
    matcher.add("SKILLS", patterns)

    doc = nlp(text.lower())
    matches = matcher(doc)

    return list({doc[start:end].text for _, start, end in matches})


def score_resume(resume_skills, job_skills):
    if not job_skills:
        return 0
    matched = set(resume_skills).intersection(set(job_skills))
    return int(len(matched) / len(job_skills) * 100)
