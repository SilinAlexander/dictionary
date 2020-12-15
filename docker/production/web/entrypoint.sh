#!/bin/sh
cd web
ls
python manage.py makemigrations
python manage.py migrate
#python manage.py runserver 0.0.0.0:8000
python manage.py collectstatic --no-input
gunicorn task.wsgi:application --bind 0.0.0.0:8000