import os
from urllib.parse import urlparse

# MySQL Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DATABASE', 'mydb'),
        'USER': os.getenv('MYSQL_USER', 'root'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD', 'password'),
        'HOST': os.getenv('MYSQL_HOST', 'db'),  # Use the container name
        'PORT': os.getenv('MYSQL_PORT', '3306'),
    }
}

# Redis Configuration
REDIS_URL = urlparse(os.getenv('REDIS_URL', 'redis://localhost:6379/0'))
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f"redis://{REDIS_URL.hostname}:{REDIS_URL.port}/{REDIS_URL.path.lstrip('/')}",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
