import fitz  # PyMuPDF
import os

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_all_resumes(folder="C:\\Users\\supong\\PycharmProjects\\ResumeJobMatcher\\data\\resumes"):
    resumes = {}
    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            path = os.path.join(folder, file)
            resumes[file] = extract_text_from_pdf(path)
    return resumes

def extract_all_jds(folder="C:\\Users\\supong\\PycharmProjects\\ResumeJobMatcher\\data\\jobs"):
    jds = {}
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
                jds[file] = f.read()
    return jds