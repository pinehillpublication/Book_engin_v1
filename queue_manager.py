import json
import os
import traceback
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
    print("=== PROCESS QUEUE STARTED ===", flush=True)

    jobs = load_jobs()

    for job in jobs:
        if job["status"] == "queued":
            try:
                print(f"Processing job: {job['job_id']}", flush=True)

                job["status"] = "in_progress"
                save_jobs(jobs)

                print("Detecting subject...", flush=True)
                subject = detect_subject(job["title"])

                print("Generating blueprint...", flush=True)
                blueprint = generate_blueprint(
                    job["title"],
                    job["level"],
                    job["pages"],
                    subject
                )

                print("Generating full book content...", flush=True)
                content = generate_full_book(job, blueprint, subject)

                print("Building LaTeX file...", flush=True)
                tex_path = build_latex(job["title"], content)

                print("Compiling PDF...", flush=True)
                compile_pdf(tex_path)

                job["status"] = "completed"
                save_jobs(jobs)

                print(f"Job completed: {job['job_id']}", flush=True)

            except Exception as e:
                print("ERROR OCCURRED:", flush=True)
                traceback.print_exc()

                job["status"] = "failed"
                job["error"] = str(e)
                save_jobs(jobs)

                print(f"Job failed: {job['job_id']}", flush=True)
