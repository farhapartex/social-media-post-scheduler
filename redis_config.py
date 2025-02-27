# redis_config.py
import os
import redis

# Load Redis configuration from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_DB = os.getenv("REDIS_DB", "0")

# Create a Redis client
redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True  # Ensures the output is a string
)

# Test the connection
try:
    redis_client.ping()
    print("Connected to Redis")
except redis.ConnectionError:
    print("Redis connection failed")
