# Base image
FROM python:3.9-slim

WORKDIR /app

# Install necessary libraries for MySQL
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV PYTHONUNBUFFERED=1

RUN python manage.py collectstatic --noinput

COPY nginx/healthcheck.py /app/

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
