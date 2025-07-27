import argparse
import json
from src.loader import load_jobs
from src.parser import extract_text_from_pdf
from src.preprocessor import preprocess
from src.matcher import compute_final_score

def main():
    parser = argparse.ArgumentParser(description='Resume AI Parser')
    parser.add_argument('--pdf', required=True)
    parser.add_argument('--job-id', required=True)
    parser.add_argument('--jobs-file', default='data/jobs.json')
    parser.add_argument('--output', default='result.json')
    args = parser.parse_args()

    jobs = load_jobs(args.jobs_file)
    job = next((j for j in jobs if j['id'] == args.job_id), None)
    if not job:
        print(f"[ERROR] Job ID '{args.job_id}' not found")
        return

    text = extract_text_from_pdf(args.pdf)
    tokens = preprocess(text)
    score = compute_final_score(tokens, text, job)

    result = {
        'job_id': job['id'],
        'job_title': job['title'],
        'score': score,
        'matched_keywords': [kw for kw in job.get('keywords', []) if kw.lower() in tokens],
        'missing_keywords': [kw for kw in job.get('keywords', []) if kw.lower() not in tokens]
    }
    with open(args.output, 'w') as f:
        json.dump(result, f, indent=2)
    print(f"[INFO] Saved to {args.output}")

if __name__ == '__main__':
    main()
