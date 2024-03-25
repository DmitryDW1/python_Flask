import databases
from fastapi.concurrency import asynccontextmanager
import sqlalchemy
from fastapi import FastAPI

DATABASE_URL = "sqlite:///lection_6/mydatabase.db"


database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

...

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
   await database.connect()
   yield
   await database.disconnect()
   print("База очищена")

app = FastAPI(lifespan=lifespan)

'''
Данный код
'''
# app = FastAPI()


# @app.on_event("startup")
# async def startup():
#     await database.connect()
    
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()
