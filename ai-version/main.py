from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task Management API")

# --- Models ---

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None


# --- In-Memory Database ---

db: List[Task] = []
id_counter: int = 1


# --- General Endpoints ---

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/health")
def healthcheck():
    return {"status": "healthy"}


# --- Specific Task Query Endpoints ---
# (Note: Defined before /tasks/{task_id} so FastAPI doesn't parse 'stats' or 'search' as integers)

@app.get("/tasks/stats")
def get_task_stats():
    total = len(db)
    done_count = sum(1 for task in db if task.done)
    undone_count = total - done_count
    return {
        "total_tasks": total,
        "completed_tasks": done_count,
        "pending_tasks": undone_count
    }

@app.get("/tasks/search", response_model=List[Task])
def search_tasks(q: str):
    return [task for task in db if q.lower() in task.title.lower()]

@app.get("/tasks/filter", response_model=List[Task])
def filter_tasks(done: bool):
    return [task for task in db if task.done == done]


# --- Core Task CRUD Endpoints ---

@app.get("/tasks", response_model=List[Task])
def get_all_tasks():
    return db

@app.get("/tasks/{task_id}", response_model=Task)
def get_task_by_id(task_id: int):
    for task in db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_in: TaskCreate):
    global id_counter
    new_task = Task(id=id_counter, title=task_in.title, done=False)
    id_counter += 1
    db.append(new_task)
    return new_task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_in: TaskUpdate):
    for task in db:
        if task.id == task_id:
            if task_in.title is not None:
                task.title = task_in.title
            if task_in.done is not None:
                task.done = task_in.done
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    for index, task in enumerate(db):
        if task.id == task_id:
            db.pop(index)
            return
    raise HTTPException(status_code=404, detail="Task not found")