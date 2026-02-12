import json
import os
from config import DATA_DIR
from subject_engine import detect_subject
from blueprint_engine import generate_blueprint
from chapter_engine import generate_full_book
from latex_builder import build_latex
from pdf_compiler import compile_pdf

JOBS_FILE = os.path.join(DATA_DIR, "jobs.json")

def load_jobs():
    if not os.path.exists(JOBS_FILE):
        return []
    with open(JOBS_FILE, "r") as f:
        return json.load(f)

def save_jobs(jobs):
    with open(JOBS_FILE, "w") as f:
        json.dump(jobs, f, indent=2)

def add_job(job):
    jobs = load_jobs()
    jobs.append(job)
    save_jobs(jobs)

def process_queue():
    jobs = load_jobs()
    for job in jobs:
        if job["status"] == "queued":
            job["status"] = "in_progress"
            save_jobs(jobs)

            subject = detect_subject(job["title"])
            blueprint = generate_blueprint(job["title"], job["level"], job["pages"], subject)
            content = generate_full_book(job, blueprint, subject)

            tex_path = build_latex(job["title"], content)
            compile_pdf(tex_path)

            job["status"] = "completed"
            save_jobs(jobs)
