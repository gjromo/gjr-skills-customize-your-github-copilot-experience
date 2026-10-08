from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    id: int
    title: str
    description: str = ""
    completed: bool = False


tasks = [
    Task(id=1, title="Plan project", description="Define the project goals.", completed=False),
    Task(id=2, title="Write code", description="Implement the feature.", completed=True),
]


@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# TODO: Add POST, PUT, and DELETE routes
# TODO: Validate input and return descriptive errors
# TODO: Test the API with FastAPI docs or curl
