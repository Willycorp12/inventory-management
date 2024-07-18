#!/bin/bash
source env/bin/activate
cd inventory_system
python manage.py runserver 0.0.0.0:8000
