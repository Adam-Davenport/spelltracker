#!/bin/bash
# This script is used to setup on a new server

# Copy bashrc file
cp .setup/.bashrc ~/.bashrc
source ~/.bashrc

# Update repository information
sudo apt update

# Web server setup
sudo apt install nginx gunicorn supervisor -y
sudo rm /etc/nginx/sites-enabled/default
sudo cp .setup/spelltracker /etc/nginx/sites-enabled/spelltracker
sudo service nginx restart

# Python setup
sudo apt install python3 -y
sudo apt install python-pip -y
pip install Django==1.11

# Galacticweapons setup
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic

# Supervisor setup
sudo cp .setup/spelltracker.conf /etc/supervisor/conf.d/spelltracker.conf
sudo service supervisor restart
