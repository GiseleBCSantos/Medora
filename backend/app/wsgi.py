"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv

load_dotenv()

from django.core.wsgi import get_wsgi_application


debug = os.getenv("DJANGO_DEBUG", "false").lower() == "true"


settings_module = (
    "app.settings.dev" if debug else "app.settings.prod"
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()
