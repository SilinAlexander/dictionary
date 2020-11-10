#!/bin/sh
cd web
ls
python manage.py makemigrations
python manage.py migrate
#python manage.py runserver 0.0.0.0:8000
gunicorn task.wsgi:application --bind 0.0.0.0:8000