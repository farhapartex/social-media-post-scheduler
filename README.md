# 📅 Social Media Post Scheduler  

This is a **FastAPI** based backend for scheduling social media posts. This project is primarily meant for practicing Docker skills and should not be used in production. I am Dockerizing this application and will later add CI/CD pipelines and more advanced DevOps practices.

---

## 🚀 **Project Overview**  
This backend API allows you to:
- Schedule posts for social media platforms.
- Manage scheduled posts with CRUD operations.
- Experiment with Docker containerization and networking.

**Note:** This project is solely for learning purposes and is not intended for production use.

---

## 📦 **Docker Setup**  

We are not using `docker-compose` for this project. Instead, the entire backend (FastAPI app + PostgreSQL database) is managed using **manual Docker commands**.

---

### 🔗 **Create Docker Network**  

Since we are not using Docker Compose, we need to create a custom network to enable communication between the backend app and the PostgreSQL database.

```bash
docker network create social_network
```

To verify the created network:
```bash
docker network ls
```

## 🗃️ Database Setup

We are using PostgreSQL 13 as our database.

1. Pull PostgreSQL Image

```bash
docker pull postgres:13
```

2. Run PostgreSQL Container

Run the PostgreSQL container on the custom network:

```bash
docker run -d \
  --name=social_db \
  --network=social_network \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=social_db \
  -p 5432:5432 \
  postgres:13
```

## 🛠️ Backend App Setup

1. Build the FastAPI App Image

```bash
docker build -t social-media-post-scheduler .
```

2. Run the FastAPI App Container

Run the backend container on the same network:

```bash
docker run -d \
  -p 8000:8000 \
  --name=sm-post-sch \
  --network=social_network \
  social-media-post-scheduler
```

## ❗ Common Error & Solution

You might encounter the following error:

```bash
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not translate host name "db" to address: Name or service not known
```

## Reason:
This occurs because the backend app cannot resolve the hostname **db**. This happens because, without **docker-compose**, the containers are not automatically placed in the same network.

## Solution:
Make sure to:

1. Create a custom network: docker network create **social_network**
2. Run both the database and backend containers on the same network using **--network=social_network**.

## 🧪 Accessing the Application

* The API will be available at: **http://localhost:8000**
* Swagger documentation is accessible at: **http://localhost:8000/docs**