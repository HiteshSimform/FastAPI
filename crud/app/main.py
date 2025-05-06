from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Dict

app = FastAPI()


@app.get("/", tags=["Index"])
async def index():
    return {"message": "Hello, ToDo...!!!"}


# ToDo
class Todo(BaseModel):
    id: Optional[int] = Field(default=None)
    title: str
    description: str | None = None
    is_completed: bool = Field(False, description="Status of ToDo")


todos = []


# create
@app.post("/todos/", response_model=Todo, status_code=201, tags=["ToDo"])
async def create_todo(todo: Todo):
    todo.id = len(todos) + 1
    todos.append(todo)
    return todo


# get
@app.get("/todos/", response_model=List[Todo], tags=["ToDo"])
async def get_todo():
    return todos


# update
# delete
