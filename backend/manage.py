#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
from multiprocessing.util import debug
import os
import sys
from dotenv import load_dotenv

load_dotenv()


def main():
    """Run administrative tasks."""
    debug = os.getenv("DJANGO_DEBUG", "false").lower() == "true"
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')


    if debug:
        settings_module = "app.settings.dev"
    else:
        settings_module = "app.settings.prod"

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
