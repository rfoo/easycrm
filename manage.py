#!~/n3bukadn3zar/django-projects/venv-easycrm/bin/python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "easycrm.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
