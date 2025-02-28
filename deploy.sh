#!/bin/bahs

docker-compose down -v
docker-compose pull
docker-compose up -d --build

# Run database migrations

docker-compose exec web alembic upgrade head

# Clean up old image

docker image prune -f