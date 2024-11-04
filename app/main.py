from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db import init_db

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Starting up...")
    await init_db(app)
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root_handler():
    return {"message": "Hello World"}
