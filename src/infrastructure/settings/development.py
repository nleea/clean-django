# coding: utf-8

from src.infrastructure.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "forex",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db-p",
        "PORT": "5432",
    }
}


# Cache
# https://docs.djangoproject.com/en/3.2/topics/cache/

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://cache:6379/1",
        "TIMEOUT": 60 * 60 * 24,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 5,
            "SOCKET_TIMEOUT": 5,
        },
    }
}
