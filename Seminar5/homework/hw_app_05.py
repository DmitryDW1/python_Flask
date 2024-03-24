# Задание №5
# Создать API для удаления информации о пользователе из базы данных.
# Приложение должно иметь возможность принимать DELETE запросы и
# удалять информацию о пользователе из базы данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Реализуйте проверку наличия пользователя в списке и удаление его из
# списка.

import uvicorn
from fastapi import FastAPI, HTTPException
from data.models import User, users



app = FastAPI()

@app.delete('/users/delete/{user_id}')
async def delete_item(user_id: int, user: User):
    for u in users:
        if u.id == user_id:
            users.remove(u)
        return {"message": 'User deleted'}
    raise HTTPException(status_code=409, detail='User not found!!!')
        

if __name__ == '__main__':
    uvicorn.run('hw_app_05:app', host='127.0.0.1', port=8000, reload=True)