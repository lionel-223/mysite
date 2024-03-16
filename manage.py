#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def check_and_create_static_dev():
    """
    Check if the static_dev directory exists, and create it if it doesn't.
    """
    base_dir = Path(__file__).resolve().parent
    static_dev_dir = base_dir / 'static_dev'
    if not static_dev_dir.exists():
        static_dev_dir.mkdir()
        print(f"Created directory: {static_dev_dir}")


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

    # Before executing any command, ensure static_dev exists and collect static files
    check_and_create_static_dev()

    if 'runserver' in sys.argv:
        # Collect static files before running the server
        os.system('python manage.py collectstatic --noinput')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
