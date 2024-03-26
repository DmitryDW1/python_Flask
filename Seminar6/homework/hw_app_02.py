# Задание №2
# Создать веб-приложение на FastAPI, которое будет предоставлять API для
# работы с базой данных пользователей. Пользователь должен иметь
# следующие поля:
# ○ ID (автоматически генерируется при создании пользователя)
# ○ Имя (строка, не менее 2 символов)
# ○ Фамилия (строка, не менее 2 символов)
# ○ Дата рождения (строка в формате "YYYY-MM-DD")
# ○ Email (строка, валидный email)
# ○ Адрес (строка, не менее 5 символов)

# Задание №2 (продолжение)
# API должен поддерживать следующие операции:
# ○ Добавление пользователя в базу данных
# ○ Получение списка всех пользователей в базе данных
# ○ Получение пользователя по ID
# ○ Обновление пользователя по ID
# ○ Удаление пользователя по ID
# Приложение должно использовать базу данных SQLite3 для хранения
# пользователей.

import datetime
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
import sqlite3


app = FastAPI()



con = sqlite3.connect('Seminar6/data/users_database_2.db')
cur = con.cursor()
cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT, 
                last_name TEXT, 
                date_of_birth DATE, 
                email TEXT, 
                address TEXT
            )
''')
con.commit()
con.close()


class User(BaseModel): # Модель для чтения из БД
    id: int
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    date_of_birth: datetime.date = Field(default=None)
    email: EmailStr | None = Field(default=None)
    address: str = Field(max_length=100)

class UserIn(BaseModel): # Модель для добавления в БД
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    date_of_birth: datetime.date = Field(default=None)
    email: EmailStr | None = Field(default=None)
    address: str = Field(max_length=100)
    


@app.get('/users')
def get_all_users():
    con = sqlite3.connect('Seminar6/data/users_database_2.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    con.close()
    return {'users': users}


@app.get('/users/{user_id}')
def get_user(user_id: int):
    con = sqlite3.connect('Seminar6/data/users_database_2.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cur.fetchone()
    con.close()
    return {'user': user}

@app.post('/users')
def create_user(user: UserIn):
    con = sqlite3.connect('Seminar6/data/users_database_2.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO users (first_name, last_name, date_of_birth, email, address) VALUES (?, ?, ?, ?, ?)''', 
                      (user.first_name, user.last_name, user.date_of_birth, user.email, user.address))
    con.commit()
    con.close()
    return {'message': 'User created successfully'}

@app.put('/users/{user_id}')
def update_user(user_id: int, user: UserIn):
    con = sqlite3.connect('Seminar6/data/users_database_2.db')
    cur = con.cursor()
    cur.execute('''UPDATE users SET first_name = ?, last_name = ?, date_of_birth = ?, email = ?, address = ? WHERE id = ?''', (user.first_name, user.last_name, user.date_of_birth, user.email, user.address, user_id))
    con.commit()
    con.close()
    return {'message': 'User updated successfully'}


@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    con = sqlite3.connect('Seminar6/data/users_database_2.db')
    cur = con.cursor()
    cur.execute('DELETE FROM users WHERE id = ?', (user_id,))
    con.commit()
    con.close()
    return {'message': 'User deleted successfully'}