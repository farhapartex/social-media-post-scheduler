#!/bin/bash

# Configuration
REPO_DIR="/home/ubuntu/social-media-post-scheduler"
GIT_REPO_URL="https://github.com/farhapartex/social-media-post-scheduler.git"
BRANCH="main"
DOCKER_COMPOSE_FILE="docker-compose.prod.yml"

echo "===== Starting Deployment ====="

# Check if the directory exists
if [ ! -d "$REPO_DIR" ]; then
    echo "Directory $REPO_DIR does not exist. Cloning the repository..."
    git clone $GIT_REPO_URL $REPO_DIR
else
    echo "Directory $REPO_DIR exists. Pulling the latest changes..."
    cd $REPO_DIR
    # Check if it's a valid Git repository
    if [ -d ".git" ]; then
        git fetch origin
        git reset --hard origin/$BRANCH
    else
        echo "ERROR: $REPO_DIR is not a valid Git repository."
        exit 1
    fi
fi

cd $REPO_DIR

echo "===== Setting Permissions ====="
chmod +x deploy.sh

echo "===== Stopping Existing Containers ====="
docker-compose -f $DOCKER_COMPOSE_FILE down -v --remove-orphans

echo "===== Pulling Latest Image from Docker Hub ====="
docker-compose -f $DOCKER_COMPOSE_FILE pull

echo "===== Starting Containers with the Latest Image ====="
docker-compose -f $DOCKER_COMPOSE_FILE up -d --build

echo "===== Running Database Migrations ====="
docker-compose -f $DOCKER_COMPOSE_FILE exec web alembic upgrade head

echo "===== Cleaning Up Old Docker Images ====="
docker image prune -f

echo "===== Deployment Completed Successfully! ====="
