# Django REST Framework with MySQL, Redis, and Docker

This project is a boilerplate for building scalable REST APIs using **Django REST Framework**, **MySQL**, and **Redis**, with complete containerization via Docker.

---

## 📁 Project Structure

myproject/
├── app/                          # Main Django application
│   ├── manage.py                 # Django CLI entry point
│   ├── myproject/                # Project settings and app
│   │   ├── __init__.py           # Python package initializer
│   │   ├── settings.py           # Configuration settings for development and production
│   │   ├── urls.py               # URL routing for the project
│   │   ├── wsgi.py               # WSGI server entry point
│   │   ├── asgi.py               # ASGI server entry point (if using async features)
│   │   ├── static/               # Collected static files
│   │   ├── media/                # Uploaded media files
├── nginx/                        # NGINX configuration
│   ├── nginx.conf                # NGINX reverse proxy configuration
│   ├── healthcheck.py            # Health check script
├── Dockerfile                    # Instructions to build the Docker image
├── docker-compose.yml            # Docker Compose file for development
├── docker-compose.prod.yml       # Docker Compose file for production
├── .env                          # Environment variables
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation


## 🛠️ Features

- **Django REST Framework** for building APIs.
- **MySQL 8.0** for relational database management.
- **Redis 6.2** for caching and task queues.
- **Gunicorn 20.1.0** and **NGINX 1.21** for production-grade deployments.
- Fully containerized using **Docker 20.10**.
- Separate configurations for **development** and **production** environments.

---

## 🚀 Getting Started

### 1. Prerequisites
- **Docker** (20.10 or newer) and **Docker Compose** (v2.6 or newer) installed on your machine.

---

### 2. Development Setup

#### Clone the repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

--->Create a .env file:

SECRET_KEY=your_secret_key
DATABASE_URL=mysql://root:password@db:3306/mydb
REDIS_URL=redis://redis:6379/0
DEBUG=True

---> Build and run the development containers:

docker-compose build
docker-compose up

--->Apply migrations and create a superuser:
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

 API: http://localhost:8000
Admin Panel: http://localhost:8000/admin


### 3. production Setup

  ---> Create a production .env file:
  
  SECRET_KEY=your_production_secret_key
  DATABASE_URL=mysql://user:password@your-managed-mysql-host:3306/mydb
  REDIS_URL=redis://your-managed-redis-host:6379/0
  DEBUG=False
  ---> Build and run the production containers:
  
  docker-compose -f docker-compose.prod.yml build
  docker-compose -f docker-compose.prod.yml up -d

🔧 Environment Variables
SECRET_KEY: Django's secret key.
DATABASE_URL: Connection string for MySQL.
REDIS_URL: Redis connection string.
DEBUG: Set to True for development and False for production.

