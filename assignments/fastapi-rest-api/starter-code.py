from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    id: int
    title: str
    description: str = ""
    completed: bool = False


tasks = [
    Task(id=1, title="Write project plan", description="Draft the scope and goals.", completed=False),
    Task(id=2, title="Review code", description="Check the latest changes.", completed=True),
]


@app.get("/tasks")
def get_tasks():
    """Return all tasks."""
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    """Return a single task by ID."""
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# TODO: Add create, update, and delete endpoints
# TODO: Validate input and handle errors cleanly
# TODO: Test the app with FastAPI's Swagger UI and /docs
