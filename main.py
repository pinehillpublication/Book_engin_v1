from fastapi import FastAPI
from pydantic import BaseModel
import uuid
import threading
from queue_manager import add_job, process_queue

app = FastAPI()

class BookRequest(BaseModel):
    title: str
    level: str
    pages: int

@app.post("/generate-book")
def generate_book(request: BookRequest):
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

    # 👇 Background thread start
    thread = threading.Thread(target=process_queue)
    thread.start()

    return {"message": "Book generation started", "job_id": job_id}
