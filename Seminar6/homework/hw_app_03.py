# Задание №3
# Создать API для управления списком задач.
# Каждая задача должна содержать поля "название",
# "описание" и "статус" (выполнена/не выполнена).
# API должен позволять выполнять CRUD операции с
# задачами.

from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI()

class Task(BaseModel): # Модель для чтения экземрляра класса из БД и добавления в БД 
    id: int 
    title: str = Field(max_length=20)
    description: str = Field(max_length=100)
    status: bool = Field(default=False)
    
class TaskIn(BaseModel): # Модель для изменения экземпляра класса в БД
    title: str = Field(max_length=20)
    description: str = Field(max_length=100)
    status: bool = Field(default=False)
    
tasks = []

@app.get('/')
async def read_root():
    return {'Hello': 'World!!!'}

@app.get('/tasks', response_model=List[Task])
async def get_tasks():
    return tasks

@app.get('/tasks/{task_id}', response_model=Task)
async def get_task(task_id: int):
    for t in tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail='Task not found')

@app.post('/tasks/', response_model=TaskIn)
async def create_task(task: Task):
    for t in tasks:
        if task.id == t.id:
            raise HTTPException(status_code=409, detail="Task exists")
    tasks.append(task)
    return task

@app.put('/tasks/{task_id}', response_model=TaskIn)
async def update_task(task_id: int, task: TaskIn):
    for t in tasks:
        if t.id == task_id:
            t.title = task.title
            t.description = task.description
            t.status = task.status
            return task
    raise HTTPException(status_code=404, detail='Task not found')

@app.put('/tasks/id/{task_id}/status/{task_status}', response_model=TaskIn)
async def update_task(task_id: int, task_status: str, task: TaskIn):
    for t in tasks:
        if t.id == task_id:
            t.status = task_status
            return task
    raise HTTPException(status_code=404, detail='Task not found')

@app.delete('/tasks/{task_id}', response_model=TaskIn)
async def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {'message': 'Task deleted'}
    raise HTTPException(status_code=404, detail='Task not found')