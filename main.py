# main.py
from fastapi import FastAPI
from database import Base, engine
from routers import posts

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(posts.router, prefix="/posts", tags=["posts"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Social Media Post Scheduler API!"}
