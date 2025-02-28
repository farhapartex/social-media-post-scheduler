#!/bin/bash

echo "Stopping existing containers..."
docker-compose -f docker-compose.prod.yml down -v --remove-orphans

echo "Pulling the latest image from Docker Hub..."
docker-compose -f docker-compose.prod.yml pull

echo "Starting containers with the latest image..."
docker-compose -f docker-compose.prod.yml up -d --build

echo "Running database migrations..."
docker-compose -f docker-compose.prod.yml exec web alembic upgrade head

echo "Cleaning up old images..."
docker image prune -f
