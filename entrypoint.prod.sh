#!/usr/bin/env bash

set -e

python manage.py makemigrations farming_v3

python manage.py collectstatic --noinput
python manage.py migrate --noinput

# after worker 3 --> <your_app_name.wsgi:application>
python -m gunicorn --bind 0.0.0.0:8000 --workers 3 mysite.wsgi:application