# Задание №4
# Создать API для обновления информации о пользователе в базе данных.
# Приложение должно иметь возможность принимать PUT запросы с данными
# пользователей и обновлять их в базе данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Реализуйте валидацию данных запроса и ответа.

import uvicorn
from fastapi import FastAPI, HTTPException
from data.models import User, users


app = FastAPI()

@app.put('/users/put/{user_id}')
async def put_user(user_id: int, user: User):
    for u in users:
        if u.id == user_id:
            u.name = user.name
            u.email = user.email
            u.password = user.password
            return user
    raise HTTPException(status_code=404, detail='User not found!!!')


if __name__ == '__main__':
    uvicorn.run('hw_app_04:app', host='127.0.0.1', port=8000, reload=True)