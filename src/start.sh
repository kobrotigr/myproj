#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py compilemessages
python manage.py runserver
