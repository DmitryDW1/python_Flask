# Задание №6
# Необходимо создать базу данных для интернет-магазина. База данных должна
# состоять из трех таблиц: товары, заказы и пользователи. Таблица товары должна
# содержать информацию о доступных товарах, их описаниях и ценах. Таблица
# пользователи должна содержать информацию о зарегистрированных
# пользователях магазина. Таблица заказы должна содержать информацию о
# заказах, сделанных пользователями.
# ○ Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY),
# имя, фамилия, адрес электронной почты и пароль.
# ○ Таблица товаров должна содержать следующие поля: id (PRIMARY KEY),
# название, описание и цена.
# ○ Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id
# пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус
# заказа.

# Задание №6 (продолжение)
# Создайте модели pydantic для получения новых данных и
# возврата существующих в БД для каждой из трёх таблиц
# (итого шесть моделей).
# Реализуйте CRUD операции для каждой из таблиц через
# создание маршрутов, REST API (итого 15 маршрутов).
# ○ Чтение всех
# ○ Чтение одного
# ○ Запись
# ○ Изменение
# ○ Удаление

import uvicorn
import shop
from data_base import database
from fastapi import FastAPI
# import hw_app_06.models.data_base as db
from fastapi.concurrency import asynccontextmanager
from asyncio import run
from typing import List
# from hw_app_06.controller.pwd_tool import hash_password
# from hw_app_06.models.model import ChangeUser, ChangeOrder, ChangeProduct, AddUser, AddOrder, AddProduct
from random import randint


@asynccontextmanager
async def lifespan(app: FastAPI):
   await database.connect()
   yield
   await database.disconnect()
    
app = FastAPI(lifespan=lifespan)
app.mount("/shop/", shop)

@app.get("/")
async def root():
    return {"message": "Главная страница"}


# if __name__ == "__main__":
#     uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=False)