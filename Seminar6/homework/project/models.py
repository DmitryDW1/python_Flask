import datetime
from pydantic import BaseModel, EmailStr, Field 

'''
Класс создания пользоателя
'''
class UserCreate(BaseModel):
    name: str = Field(max_length=20)
    surname: str = Field(max_length=30)
    email: EmailStr | None = Field(default=None)
    password: str = Field(min_length=3)

'''
Класс чтения информации о пользователе
'''
class UserRead(BaseModel):
    id: int
    surname: str = Field(max_length=30)
    email: EmailStr | None = Field(default=None)
    password: str = Field(min_length=3)

'''
Класс создания товара
'''
class ProductCreate(BaseModel):
    title: str = Field(max_length=50)
    description: str = Field(max_length=300)
    price: int = Field(default=0)

'''
Класс чтения информации о товаре
'''
class ProductRead(BaseModel):
    id: int
    title: str = Field(max_length=50)
    description: str = Field(max_length=300)
    price: int = Field(default=0)

'''
Класс создания заказа
'''
class OrderCreate(BaseModel):
    user_id: int
    prod_id: int
    date: datetime.date = Field(default=datetime.date)
    status: str = Field(default="created")

'''
Класс чтения информации о заказе
'''
class OrderRead(BaseModel):
    id: int
    prod_id: int
    date: datetime.date = Field(default=datetime.date)
    status: str = Field(default="created")