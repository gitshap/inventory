#!/bin/bash
makemigrations='python manage.py makemigrations equipment'
migrate='python manage.py migrate equipment'

eval $makemigrations
eval $migrate