# Задание №6
# Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.

from fastapi.responses import HTMLResponse
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from data.models import User, users
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='./Seminar5/homework/templates')

# @app.get('/{name}', response_class=HTMLResponse)
# async def read_item(request: Request, name: str):
#     print(request)
#     return templates.TemplateResponse('item.html', {'request': request, 'name': name})

@app.get('/users/', response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse('item.html', {'request': request, 'users': users})
    
@app.post('/users/', response_model=User)
async def create_user(new_user: User):
    for user in users:
        if user.id == new_user.id:
            raise HTTPException(status_code=400, detail='User already exists')
    users.append(new_user)
    return new_user

@app.put('/users/put/{user_id}')
async def put_user(user_id: int, user: User):
    for u in users:
        if u.id == user_id:
            u.name = user.name
            u.email = user.email
            u.password = user.password
            return user
    raise HTTPException(status_code=404, detail='User not found!!!')

@app.delete('/users/delete/{user_id}')
async def delete_item(user_id: int, user: User):
    for u in users:
        if u.id == user_id:
            users.remove(u)
        return {'message": "User deleted'}
    raise HTTPException(status_code=409, detail='User not found!!!')
    
            
if __name__ == '__main__':
    uvicorn.run('hw_app_06:app', host='127.0.0.1', port=8000, reload=True)