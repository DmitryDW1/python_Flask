# Задание №2
# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.

from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Movie(BaseModel):
    id: int 
    title: str 
    description: str 
    genre: str 
    
movies = [
    Movie(id=1, title='Один дома', description="Description 1", genre="Comedy"),
    Movie(id=2, title="Рататуй", description="Description 2", genre="Comedy"),
    Movie(id=3, title="9 рота", description="Description 3", genre="Action"),
    Movie(id=4, title="Достучаться до небес", description="Description 3", genre="Drama"),
    Movie(id=5, title="Вокзал для двоих", description="Description 3", genre="Drama"),
    Movie(id=6, title="Зловещие мертвецы 1", description="Description 4", genre="Horror"),
]

@app.get('/')
async def read_root():
    return f'Список жанров: Comedy, Action, Drama, Horror'

@app.get('/movies/{u_genre}', response_model=List[Movie])
async def get_movies(u_genre):
    sorted_movies = []
    for movie in movies:
        if movie.genre == u_genre.capitalize():
            sorted_movies.append(movie)
    if len(sorted_movies) != 0:
        return sorted_movies
    else:
        raise HTTPException(status_code=404, detail="Фильмы не найдены")

if __name__ == '__main__':
    uvicorn.run('hw_app_02:app', host='127.0.0.1', port=8000, reload=True)