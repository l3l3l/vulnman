#!/bin/bash


# Apply database migrations
echo "Apply database migrations"
python manage.py migrate


# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput


python manage.py create_secret_key

# create superuser
echo "Create superuser"
python manage.py createsuperuser --noinput

# Start server
echo "Starting server"
gunicorn --bind 0.0.0.0:8000 vulnman.wsgi