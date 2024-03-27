import database as db
from typing import List
from fastapi import HTTPException, APIRouter
from models import OrderCreate, OrderRead, ProductCreate, ProductRead, UserCreate, UserRead


app = APIRouter()

@app.get('/')   
def root():
    return f'Итоговая работа'


@app.post('/users/', response_model=UserRead)    
async def create_users(user: UserCreate):
    '''
    Создание пользоателя
    '''
    query = db.users.insert().values(name=user.name, surname=user.surname, email=user.email, password=user.password)
    query = db.users.insert().values(**user.model_dump())
    last_record_id = await db.database.execute(query)  
    return {**user.model_dump(), 'id': last_record_id}  


@app.post('/products/', response_model=ProductRead)
async def create_products(product: ProductCreate):
    '''
    Создание товара
    '''
    query = db.products.insert().values(title=product.title, description=product.description, price=product.price)
    query = db.products.insert().values(**product.model_dump())
    last_record_id = await db.database.execute(query)
    return {**product.model_dump(), 'id': last_record_id}


@app.post('/orders/{id_user}/{id_product}', response_model=OrderRead)
async def create_orders(id_user: int, id_product: int, order: OrderCreate):
    '''
    Создание заказа
    ''' 
    query = db.orders.insert().values(user_id=id_user, prod_id=id_product, status="created")
    query = db.orders.insert().values(**order.model_dump())
    last_record_id = await db.database.execute(query)
    return {**order.model_dump(), 'id': last_record_id}


@app.get("/users/", response_model=List[UserRead]) 
async def read_users():
    '''
    Чтение информации о всех пользователях
    '''
    query = db.users.select()
    return await db.database.fetch_all(query)


@app.get("/products/", response_model=List[ProductRead])
async def read_products():
    '''
    Чтение информации о всех тоарах
    '''
    query = db.products.select()
    return await db.database.fetch_all(query)


@app.get("/orders/", response_model=List[OrderRead])
async def read_orders():
    '''
    Чтение информации о всех заказах
    '''
    query = db.orders.select()
    return await db.database.fetch_all(query)


@app.get("/users/{user_id}", response_model=UserRead)
async def read_user(user_id: int):
    '''
    Чтение информации о пользователе по id
    '''
    query = db.users.select().where(db.users.c.id == user_id) 
    user = await db.database.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found") 
    return user


@app.get("/products/{product_id}", response_model=ProductRead)
async def read_product(product_id: int):
    '''
    Чтение информации о товаре по id
    '''
    query = db.products.select().where(db.products.c.id == product_id)
    product = await db.database.fetch_one(query)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.get("/orders/{order_id}", response_model=OrderRead)
async def read_order(order_id: int):
    '''
    Чтение информации о заказе по id
    '''
    query = db.orders.select().where(db.orders.c.id == order_id)
    order = await db.database.fetch_one(query)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@app.put("/users/{user_id}", response_model=UserRead)
async def update_user(user_id: int, new_user: UserCreate):
    '''
    Изменение информации о пользователе по id
    '''
    query = db.users.update().where(db.users.c.id == user_id).values(**new_user.dict())
    await db.database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.put("/products/{product_id}", response_model=ProductRead)
async def update_product(product_id: int, new_product: ProductCreate):
    '''
    Изменение информации о товаре по id
    '''
    query = db.products.update().where(db.products.c.id == product_id).values(**new_product.model_dump())
    await db.database.execute(query)
    return {**new_product.dict(), "id": product_id}


@app.put("/orders/{order_id}", response_model=OrderRead)
async def update_order(order_id: int, new_order: OrderCreate):
    '''
    Изменение информации о заказе по id
    '''
    query = db.orders.update().where(db.orders.c.id == order_id).values(**new_order.model_dump())
    await db.database.execute(query)
    return {**new_order.dict(), "id": order_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    '''
    Удаление информации о пользователе по id
    '''
    query = db.users.delete().where(db.users.c.id == user_id)
    await db.database.execute(query)
    return {'message': 'User deleted'}


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    '''
    Удаление информации о товаре по id
    '''
    query = db.products.delete().where(db.products.c.id == product_id)
    await db.database.execute(query)
    return {'message': 'Product deleted'}


@app.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    '''
    Удаление информации о заказе по id
    '''
    query = db.orders.delete().where(db.orders.c.id == order_id)
    await db.database.execute(query)
    return {'message': 'Order deleted'}
