# 📅 Social Media Post Scheduler  

This is a **FastAPI** based backend for scheduling social media posts. This project is primarily meant for practicing **Docker**, **Docker Compose**, **Redis**, and **Celery** skills and should not be used in production. 

I am continuously enhancing this application by integrating advanced **DevOps** practices, including **CI/CD pipelines** and **background task management**.

---

## 🚀 **Project Overview**  
This backend API allows you to:
- Schedule posts for social media platforms.
- Manage scheduled posts with CRUD operations.
- **Redis** for caching and message brokering.
- **Celery** for background tasks (e.g., scheduling posts).
- **Docker Compose** for managing multi-container setup.

**Note:** This project is solely for learning purposes and is not intended for production use.

---

## 📦 **Tech Stack**  
- **FastAPI**: Web framework for building APIs.
- **PostgreSQL**: Relational database.
- **Redis**: Caching and message broker for Celery.
- **Celery**: Background task management.
- **Docker Compose**: Multi-container orchestration.
- **Docker**: Containerization platform.

---


## 📝 **Environment Variables**  
The application uses the following environment variables:

- `POSTGRES_USER`: PostgreSQL username
- `POSTGRES_PASSWORD`: PostgreSQL password
- `POSTGRES_DB`: PostgreSQL database name
- `POSTGRES_HOST`: Hostname for PostgreSQL (`db` in Docker Compose)
- `POSTGRES_PORT`: PostgreSQL port (`5432`)
- `REDIS_HOST`: Hostname for Redis (`redis` in Docker Compose)
- `REDIS_PORT`: Redis port (`6379`)
- `REDIS_DB`: Redis database index (`0`)

These variables are configured in the `docker-compose.yml` file.

---

## 🛠️ **Setup and Installation**  

### 1. **Clone the Repository**  
```bash
git clone git@github.com:farhapartex/social-media-post-scheduler.git
cd social-media-post-scheduler
```

---

### 2. **Build and Run with Docker Compose**
```bash
docker-compose up --build
```

**To Stop the Containers:**
```bash
docker-compose down -v
```

### Accessing the Application

* FastAPI: http://localhost:8000
* Swagger Documentation: http://localhost:8000/docs