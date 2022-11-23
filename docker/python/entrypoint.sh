#!/bin/bash

/MENTIZ/docker/python/wait-for-it.sh db:3306 -- python /MENTIZ/manage.py migrate
gunicorn MENTIZ.wsgi:application --bind 0.0.0.0:8000