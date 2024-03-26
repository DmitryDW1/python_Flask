from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class User(BaseModel): # Модель для чтения экземрляра класса из БД и добавления в БД 
    id: int
    first_name: str = Field(max_length=80)
    last_name: str = Field(max_length=80)
    user_email: EmailStr | None = Field(default=None)
    password: str = Field(max_length=280)

class Order(BaseModel): # Модель для чтения экземрляра класса из БД и добавления в БД
    id: int
    id_user: int
    id_product: int
    data_order: datetime = Field(datetime.now())
    status_order: str = Field(20)

class Product(BaseModel): # Модель для чтения экземрляра класса из БД и добавления в БД
    id: int
    name_product: str = Field(max_length=100)
    description_product: str = Field(max_length=360)
    price_product: int = Field(default=0)

class UserIn(BaseModel): # Модель для изменения экземпляра класса в БД
    first_name: str = Field(max_length=80)
    last_name: str = Field(max_length=80)
    user_email: EmailStr | None = Field(default=None)
    password: str = Field(max_length=280)

class OrderIn(BaseModel): # Модель для изменения экземпляра класса в БД
    id_user: int
    id_product: int
    data_order: datetime = Field(datetime.now())
    status_order: str = Field(20)

class ProductIn(BaseModel): # Модель для изменения экземпляра класса в БД
    name_product: str = Field(max_length=100)
    description_product: str = Field(max_length=360)
    price_product: int = Field(default=0)