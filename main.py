from fastapi import FastAPI, HTTPException , Response
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
    raise HTTPException(status_code=404, detail="Task not found")


 
@app.post("/tasks",status_code=201)
def create_task(task: dict):
    task["id"] = len(tasks) + 1
    task["done"] = False
    tasks.append(task)
    return { "message": "Task created successfully" }


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: dict):

    if set(task.keys()) - {"title", "done"}:
        raise HTTPException(status_code=400, detail="Invalid body")
    for tsk in tasks:
        if tsk["id"] == task_id:
            if "title" in task:
                tsk["title"] = task["title"]
            if "done" in task:
                tsk["done"] = task["done"]
            return tsk

    raise HTTPException(status_code=404, detail="Task not found")



@app.delete("/tasks/{task_id}",status_code=204)
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return Response(status_code=204)
    return HTTPException(status_code=404, detail="Task not found")
    