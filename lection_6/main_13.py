from typing import List
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field

DATABASE_URL = "sqlite:///lection_6/mydatabase.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)

engine = sqlalchemy.create_engine(
DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

app = FastAPI()


class UserIn(BaseModel): # Модель для добавления в БД
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)
    
    
class User(BaseModel): # Модель для чтения из БД
    id: int
    name: str = Field(max_length=32)
    email: str = Field(max_length=128)
    
# '''
# Данный метод создания тестовых данных должен использоваться только при разработке и тестировании
# '''
# @app.get("/fake_users/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         query = users.insert().values(name=f'user{i}', email=f'mail{i}@mail.ru')
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}

@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email)
    # query = users.insert().values(**user.dict()) # устаревший метод .dict()
    query = users.insert().values(**user.model_dump())
    last_record_id = await database.execute(query)
    # return {**user.dict(), "id": last_record_id} # устаревший метод .dict()
    return {**user.model_dump(), "id": last_record_id}

@app.get("/users/", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 3): # Применение выборки по количеству выводимой информации. Продолжение в следующей строке
    query = users.select().limit(limit).offset(skip)
    return await database.fetch_all(query)

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)

@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    await database.execute(query)
    return {**new_user.model_dump(), "id": user_id}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}