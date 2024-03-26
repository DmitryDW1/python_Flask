# Задание №8
# Необходимо создать API для управления списком задач. Каждая задача должна
# содержать заголовок и описание. Для каждой задачи должна быть возможность
# указать статус (выполнена/не выполнена).
# API должен содержать следующие конечные точки:
# ○ GET /tasks - возвращает список всех задач.
# ○ GET /tasks/{id} - возвращает задачу с указанным идентификатором.
# ○ POST /tasks - добавляет новую задачу.
# ○ PUT /tasks/{id} - обновляет задачу с указанным идентификатором.
# ○ DELETE /tasks/{id} - удаляет задачу с указанным идентификатором.
# Для каждой конечной точки необходимо проводить валидацию данных запроса и
# ответа. Для этого использовать библиотеку Pydantic.

from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
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

@app.put('/tasks/id/{task_id}/status/{task_status}', response_model=Task)
async def update_task(task_id: int, task_status: str, task: Task):
    for t in tasks:
        if t.id == task_id:
            t.status = task_status
            return task
    raise HTTPException(status_code=404, detail='Task not found')

@app.delete('/tasks/{task_id}', response_model=Task)
async def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {'message': 'Task deleted'}
    raise HTTPException(status_code=404, detail='Task not found')



if __name__ == '__main__':
    uvicorn.run('hw_app_08:app', host='127.0.0.1', port=8000, reload=True)
    