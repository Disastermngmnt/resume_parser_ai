# 1. Clone the repo and navigate into it:
        git clone <repo-url>
        cd resume_parser

# 2. Create and activate a virtual environment:
        python3 -m venv venv
        source venv/bin/activate   # (Windows: venv\Scripts\activate)

# 3. Install dependencies:
    pip install -r requirements.txt
     Ensure requirements.txt includes:
     pdfplumber
     nltk
     gemma3-sdk
     (optional) langchain, faiss-cpu

# 4. Download NLTK data (once):
    python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

# 5. Populate job definitions:
    Edit data/jobs.json with your job entries:
    [
      {
        "id": "SWE-1",
        "title": "Software Engineer",
        "keywords": ["Python","APIs","Docker"],
        "references": ["3+ years backend experience","microservices"]
      }
    ]

# 6. Run the parser:
    python -m src.cli --pdf path/to/resume.pdf --job-id SWE-1 --jobs-file data/jobs.json --output result.json

    - --pdf:    Path to the resume PDF file
    - --job-id: The ID of the job posting to match (from jobs.json)
    - --jobs-file: Optional path to your jobs.json (default: data/jobs.json)
    - --output: Path for the JSON result (default: result.json)

# 7. Inspect the result.json for:
    {
      "job_id": "SWE-1",
      "job_title": "Software Engineer",
      "score": 78,
      "matched_keywords": ["Python","Docker"],
      "missing_keywords": ["APIs"]
    }

# 8. Common adjustments:
    - If PDF is scanned/has no text, integrate OCR in src/parser.py
    - Tweak weights in matcher.py (70/30 exact vs semantic)
    - For LangChain integration, uncomment the snippet in matcher.py
