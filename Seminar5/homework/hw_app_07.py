# Задание №7
# Создать RESTful API для управления списком задач. Приложение должно
# использовать FastAPI и поддерживать следующие функции:
# ○ Получение списка всех задач.
# ○ Получение информации о задаче по её ID.
# ○ Добавление новой задачи.
# ○ Обновление информации о задаче по её ID.
# ○ Удаление задачи по её ID.
# Каждая задача должна содержать следующие поля: ID (целое число),
# Название (строка), Описание (строка), Статус (строка): "todo", "in progress",
# "done".
# Погружение в Python
# Задание №7 (продолжение)
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте функцию get_tasks для получения списка всех задач (метод GET).
# Создайте функцию get_task для получения информации о задаче по её ID
# (метод GET).
# Создайте функцию create_task для добавления новой задачи (метод POST).
# Создайте функцию update_task для обновления информации о задаче по её ID
# (метод PUT).
# Создайте функцию delete_task для удаления задачи по её ID (метод DELETE).

import random
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()
list_task_status = ['todo', 'in progress', 'done']

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
async def get_tasks():
    return tasks

@app.get('/tasks/{task_id}', response_model=Task)
async def get_task(task_id: int):
    for t in tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail='Task not found')

@app.post('/tasks/', response_model=Task)
async def create_task(task: Task):
    for t in tasks:
        if task.id == t.id:
            raise HTTPException(status_code=409, detail="Task exists")
    task.status = random.choice(list_task_status)
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
    raise HTTPException(status_code=404, detail='Task not found')

@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {'message': 'Task deleted'}
    raise HTTPException(status_code=404, detail='Task not found')



if __name__ == '__main__':
    uvicorn.run('hw_app_07:app', host='127.0.0.1', port=8000, reload=True)
    