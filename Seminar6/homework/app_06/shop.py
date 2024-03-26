import datetime
from fastapi import FastAPI, HTTPException
from data import database as db
from passlib.context import CryptContext
# from asyncio import run
from typing import List
from pwd_tool import hash_password
from model import User, Order, Product, UserIn, OrderIn, ProductIn



shop = FastAPI(title='Домашняя работа №6')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@shop.get("/users/", response_model=List[User])
async def read_users():
    query = db.users.select()
    users = await db.database.fetch_all(query)
    if users:
        return users
    raise HTTPException(status_code=404, detail="Не найдено ни одного пользователя")

@shop.get("/users/{id_user}", response_model=User)
async def read_users_id(id_user: int):
    query = db.users.select().where(db.users.c.id == id_user)
    user = await db.database.fetch_one(query)
    if user:
        return user
    raise HTTPException(status_code=404, detail="Не найдено ни одного пользователя")


@shop.get("/products/", response_model=List[Product])
async def read_products():
    query = db.products.select()
    products = await db.database.fetch_all(query)
    if products:
        return products
    raise HTTPException(status_code=404, detail="Не найдено ни одного продукта")


@shop.get("/products/{id_product}", response_model=Product)
async def read_products_id(id_product: int):
    query = db.products.select().where(db.products.c.id == id_product)
    product = await db.database.fetch_one(query)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Не найдено ни одного продукта")


@shop.get("/orders/", response_model=List[Order])
async def change_users():
    query = db.orders.select()
    orders = await db.database.fetch_all(query)
    if orders:
        return orders
    raise HTTPException(status_code=404, detail="Не найдено ни одного заказа")


@shop.get("/orders/{id_orders}", response_model=Order)
async def read_products_id(id_orders: int):
    query = db.orders.select().where(db.orders.c.id == id_orders)
    order = await db.database.fetch_one(query)
    if order:
        return order
    raise HTTPException(status_code=404, detail="Не найдено ни одного заказа")

@shop.put("/users/{id_user}", response_model=UserIn)
async def user_update(id_user: int, new_user: UserIn):
    hashed_password = await hash_password(new_user.password)
    new_user = new_user.dict()
    new_user['password'] = hashed_password
    query = db.users.update().where(db.users.c.id == id_user).values(**new_user)
    await db.database.execute(query)
    return {**new_user, "id": id_user}


@shop.put("/products/{id_product}", response_model=ProductIn)
async def product_update(id_product: int, new_product: ProductIn):
    query = db.products.update().where(db.products.c.id == id_product).values(**new_product.dict())
    await db.database.execute(query)
    return {**new_product.dict(), "id": id_product}


@shop.put("/orders/{id_orders}", response_model=OrderIn)
async def order_update(id_orders: int, new_order: OrderIn):
    query = db.orders.update().where(db.orders.c.id == id_orders).values(**new_order.dict())
    await db.database.execute(query)
    return {**new_order.dict(), "id": id_orders}


@shop.delete("/users/{id_user}")
async def user_delete(id_user: int):
    query = db.users.delete().where(db.users.c.id == id_user)
    user = await db.database.execute(query)
    if user:
        return {'message': 'Пользователь удален'}
    raise HTTPException(status_code=404, detail="Не найдено пользователя")


@shop.delete("/products/{id_product}")
async def product_delete(id_product: int):
    query = db.products.delete().where(db.products.c.id == id_product)
    product = await db.database.execute(query)
    if product:
        return {'message': 'Продукт удален'}
    raise HTTPException(status_code=404, detail="Не найдено продукта")


@shop.delete("/orders/{id_orders}")
async def order_delete(id_orders: int):
    query = db.orders.delete().where(db.orders.c.id == id_orders)
    order = await db.database.execute(query)
    if order:
        return {'message': 'Заказ удален'}
    raise HTTPException(status_code=404, detail="Не найдено заказа")

@shop.post('/users/', response_model=UserIn)
async def user_add(new_user: UserIn):
    hashed_password = await hash_password(new_user.password)
    new_user = new_user.dict()
    query = db.users.insert().values(first_name=new_user['first_name'],
                                     last_name=new_user['last_name'],
                                     user_email=new_user['user_email'],
                                     password=hashed_password)
    await db.database.execute(query)
    return {**new_user}


@shop.post('/products/', response_model=ProductIn)
async def product_add(new_product: ProductIn):
    new_product = new_product.dict()
    query = db.products.insert().values(name_product=new_product['name_product'],
                                        description_product=new_product['description_product'],
                                        price_product=new_product['price_product'])
    await db.database.execute(query)
    return {**new_product}


@shop.post('/orders/', response_model=OrderIn)
async def order_add(new_order: OrderIn):
    new_order = new_order.dict()
    query = db.orders.insert().values(id_user=new_order['id_user'],
                                      id_product=new_order['id_product'],
                                      data_order=datetime.datetime.now(),
                                      status_order=new_order['status_order'])
    await db.database.execute(query)
    return {**new_order}