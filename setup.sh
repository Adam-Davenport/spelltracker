#!/bin/bash
# This script is used to setup on a new server

# Copy bashrc file
cp .setup/.bashrc ~/.bashrc
source ~/.bashrc

# Update repository information
sudo apt update

# Web server setup
sudo apt install nginx gunicorn upstart -y
sudo rm /etc/nginx/sites-enabled/default
sudo cp .setup/spelltracker /etc/nginx/sites-enabled/spelltracker
sudo service nginx restart

# Python setup
sudo apt install python3
sudo apt install python-pip
pip install Django==1.11

# Galacticweapons setup
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic

# Supervisor setup
sudo cp .setup/gunicorn.conf /etc/init/gunicorn.conf
sudo service supervisor restart
