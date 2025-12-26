"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from dotenv import load_dotenv

load_dotenv()

from django.core.asgi import get_asgi_application

debug = os.getenv("DJANGO_DEBUG", "false").lower() == "true"

settings_module = (
    "app.settings.dev" if debug else "app.settings.prod"
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgi_application()
