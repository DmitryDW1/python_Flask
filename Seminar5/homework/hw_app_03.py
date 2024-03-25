# Задание №3
# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.

import uvicorn
from fastapi import FastAPI, HTTPException
from data.models import User, users



app = FastAPI()


@app.post('/users/', response_model=User)
async def create_user(new_user: User):
    for user in users:
        if user.id == new_user.id:
            raise HTTPException(status_code=400, detail='User already exists')
    users.append(new_user)
    return new_user

    
            
if __name__ == '__main__':
    uvicorn.run('hw_app_03:app', host='127.0.0.1', port=8000, reload=True)