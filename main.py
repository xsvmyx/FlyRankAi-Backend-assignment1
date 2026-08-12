from fastapi import FastAPI, HTTPException
from tasks import tasks


app = FastAPI()


@app.get("/")
def read_root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }



@app.get("/health")
def health_check():
    return { "status": "ok" }




@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return HTTPException(status_code=404, detail="Task not found")