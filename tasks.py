# tasks.py
from celery_config import celery_app
from time import sleep

@celery_app.task(name="create_post_task")
def create_post_task(content):
    print("Creating post...")
    sleep(5)  # Simulate a delay
    print(f"Post created with content: {content}")
    return f"Post created with content: {content}"
