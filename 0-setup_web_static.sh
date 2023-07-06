#!/usr/bin/env bash
# Bash script to setupand configure nginx
# It also creates relevant directories and sub-directories

# Install nginx
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Create directories and subdirectories
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Create a fake HTML file
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link -f
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change Ownership of folder
sudo chown -hR ubuntu:ubuntu /data/

# Configure nginx
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx start
