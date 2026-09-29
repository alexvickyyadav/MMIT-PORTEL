#!/bin/bash
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt
echo "Starting MPIT Shravasti Server on http://127.0.0.1:8000/"
python manage.py runserver
