# Задание №1
# Создать API для управления списком задач. Приложение должно иметь
# возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.

from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
import uvicorn

app = FastAPI()


class Task(BaseModel):
    id: int 
    title: str 
    description: str 
    status: str 
    
tasks = []


@app.get('/')
async def read_root():
    return {'Hello': 'World!!!'}

@app.get('/tasks', response_model=List[Task])
async def get_task():
    return tasks

@app.post('/tasks', response_model=Task)
async def post_task(task: Task):
    for t in tasks:
        if task.id == t.id:
            raise HTTPException(status_code=409, detail="Task exists")
    tasks.append(task)
    return task

@app.put('/tasks/{task_id}', response_model=Task)
async def update_task(task_id: int, task: Task):
    for t in tasks:
        if t.id == task_id:
            t.title = task.title
            t.description = task.description
            t.status = task.status
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

if __name__ == '__main__':
    uvicorn.run('hw_app_01:app', host='127.0.0.1', port=8000, reload=True)
    