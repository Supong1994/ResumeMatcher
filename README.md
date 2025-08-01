# ResumeMatcher
Resume Parser and Job Matcher
Project Structure
bash
Copy
Edit
ResumeJobMatcher/
├── data/                # Raw input files
│   ├── resumes/         # Contains text versions of resumes
│   └── jobs/            # Contains job descriptions (JDs)
├── notebooks/
│   └── EDA.ipynb        # Jupyter notebook for running matching logic
├── src/                 # Core Python modules
│   ├── extractor.py     # Functions to load and clean text data
│   ├── vectorizer.py    # Vectorization model (e.g., TF-IDF or BERT)
│   ├── matcher.py       # Scoring logic between resume and JD
│   └── __init__.py      # Makes src a package

Modular Code Design:

Separated logic into three core modules: extractor.py, vectorizer.py, and matcher.py.

Dynamic Import Setup:

Used sys.path to dynamically resolve import paths so you can run everything from the notebooks/EDA.ipynb file without import errors.

Resume & JD Parsing:

Implemented in extractor.py. Reads .txt files from data/resumes/ and data/jobs/.

Vectorization (NLP):

Defined a model in vectorizer.py using TF-IDF or another NLP technique to convert text into numeric vectors.

Matching Logic:

matcher.py compares each resume against each JD using cosine similarity and returns a match score.

Notebook Execution:

EDA.ipynb demonstrates how all components work together to score resume-JD matches.

📊 Sample Output
rust
Copy
Edit
resume1.txt -> jd1.txt = 0.82
resume1.txt -> jd2.txt = 0.68
resume2.txt -> jd1.txt = 0.75
