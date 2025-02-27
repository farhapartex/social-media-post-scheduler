# main.py
from fastapi import FastAPI
from redis_config import redis_client
from tasks import create_post_task
from database import Base, engine
from routers import posts

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(posts.router, prefix="/posts", tags=["posts"])

@app.get("/")
def read_root():
    redis_client.set("message", "Welcome to Social Media Post Scheduler API!")
    message = redis_client.get("message")
    return {"message": message}


# API to trigger celery task
@app.post("/test_celery_task/")
def schedule_post(content: str):
    task = create_post_task.delay(content)
    return {"task_id": task.id, "status": "Post is being scheduled"}
