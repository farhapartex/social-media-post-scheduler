# celery_config.py
from celery import Celery
import os

# Load Redis configuration from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_DB = os.getenv("REDIS_DB", "0")

# Redis URL for Celery Broker
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

# Create Celery instance
celery_app = Celery(
    "social_media_scheduler",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["tasks"]  # Include tasks from the tasks module
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
