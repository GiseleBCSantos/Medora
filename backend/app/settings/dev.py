from .base import *
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = True

SECRET_KEY = os.getenv('SECRET_KEY', 'unsafe-dev-key')

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ALLOW_ALL_ORIGINS = True
