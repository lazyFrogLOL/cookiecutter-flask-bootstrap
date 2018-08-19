#!/bin/sh
source venv/bin/activate
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - {{cookiecutter.app_name}}:{{cookiecutter.app_name}}