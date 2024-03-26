# Задание №4
# Напишите API для управления списком задач. Для этого создайте модель Task
# со следующими полями:
# ○ id: int (первичный ключ)
# ○ title: str (название задачи)
# ○ description: str (описание задачи)
# ○ done: bool (статус выполнения задачи)

# Задание №4 (продолжение)
# API должно поддерживать следующие операции:
# ○ Получение списка всех задач: GET /tasks/
# ○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
# ○ Создание новой задачи: POST /tasks/
# ○ Обновление информации о задаче: PUT /tasks/{task_id}/
# ○ Удаление задачи: DELETE /tasks/{task_id}/
# Для валидации данных используйте параметры Field модели Task.
# Для работы с базой данных используйте SQLAlchemy и модуль databases.

from typing import List
import databases
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import sqlalchemy

DATABASE_URL = "sqlite:///Seminar6/data/task_database.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(20)),
    sqlalchemy.Column("description", sqlalchemy.String(100)),
    sqlalchemy.Column("done", sqlalchemy.BOOLEAN(False)),
)

engine = sqlalchemy.create_engine(
DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

app = FastAPI()

class Task(BaseModel): # Модель для чтения экземрляра класса из БД и добавления в БД 
    id: int 
    title: str = Field(max_length=20)
    description: str = Field(max_length=100)
    done: bool = Field(default=False)
    
class TaskIn(BaseModel): # Модель для изменения экземпляра класса в БД
    title: str = Field(max_length=20)
    description: str = Field(max_length=100)
    done: bool = Field(default=False)

@app.get('/')
async def read_root():
    return {'Hello': 'World!!!'}

@app.get('/tasks', response_model=List[Task])
async def get_tasks():
    query = tasks.select()
    return await database.fetch_all(query)

@app.get('/tasks/{task_id}', response_model=Task)
async def get_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    if query:
        return await database.fetch_one(query)
    raise HTTPException(status_code=404, detail='Task not found')

@app.post('/tasks/', response_model=Task)
async def create_task(task: TaskIn):
    query = tasks.insert().values(title=task.title, description=task.description, done=task.done)
    query = tasks.insert().values(**task.model_dump())
    last_record_id = await database.execute(query)
    return {**task.model_dump(), 'id': last_record_id}

@app.put('/tasks/{task_id}', response_model=Task)
async def update_task(task_id: int, new_task: TaskIn):
    query = tasks.update().where(tasks.c.id == task_id).values(**new_task.model_dump())
    await database.execute(query)
    return {**new_task.model_dump(), "id": task_id}


@app.delete('/tasks/{task_id}', response_model=Task)
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    if query:
        await database.execute(query)
    raise HTTPException(status_code=404, detail='Task not found')