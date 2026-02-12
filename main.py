from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import uuid
from queue_manager import add_job, process_queue
from config import OUTPUT_DIR

app = FastAPI()

class BookRequest(BaseModel):
    title: str
    level: str
    pages: int

@app.post("/generate-book")
def generate_book(request: BookRequest, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())

    job = {
        "job_id": job_id,
        "title": request.title,
        "level": request.level,
        "pages": request.pages,
        "status": "queued",
        "current_chapter": 0
    }

    add_job(job)
    background_tasks.add_task(process_queue)

    return {"message": "Book generation started", "job_id": job_id}
