import json
from typing import List, Dict

def load_jobs(path: str) -> List[Dict]:
    print(path)
    """
    Load job postings from a JSON file.
    Each job entry must include:
      - id: unique string (e.g. "SWE-1")
      - title: human‑readable job title
      - keywords: list of required keywords to match exactly
      - references: list of free‑text statements for semantic matching
    """
    with open("C:\Users\ayush\Downloads\resume_parser_with oolam\resume_parser\data\jobs.json", 'r', encoding='utf-8') as f:
        jobs = json.load(f)
    print(jobs)
    for job in jobs:
        assert 'id' in job, "Every job must have an 'id'"
        assert 'title' in job, "Every job must have a 'title'"
        assert isinstance(job.get('keywords', []), list), "'keywords' must be a list"
        assert isinstance(job.get('references', []), list), "'references' must be a list"
    return jobs
jobs = load_jobs("jobs.json")
print(jobs)