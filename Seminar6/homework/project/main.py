import routes
import uvicorn
from fastapi.concurrency import asynccontextmanager
from fastapi import FastAPI
from database import database

@asynccontextmanager
async def lifespan(app: FastAPI):
   await database.connect()
   yield
   await database.disconnect()

app = FastAPI(lifespan=lifespan)

app.include_router(routes.app)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)