#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status.

echo "Updating Packages and Installing Requirements"

# Update Package Manager
sudo apt-get update
sudo apt-get install -y nginx python3-pip net-tools gunicorn

# Install Python packages
pip install flask flask_cors sqlalchemy

# Remove any current AIRBNB Repository
rm -rf AirBnB_clone_v*

# Clone Repositories
git clone https://github.com/highrate01/AirBnB_clone_v2
git clone https://github.com/highrate01/AirBnB_clone_v3
git clone https://github.com/highrate01/AirBnB_clone_v4

# Define the path to the Nginx configuration file to be overwritten
NGINX_CONFIG="/etc/nginx/sites-enabled/default"

# Overwrite the Nginx configuration file with the provided configuration
sudo tee "$NGINX_CONFIG" > /dev/null <<EOF
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    add_header X-Served-By \$hostname;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
    location /static/ {
        alias /home/ubuntu/AirBnB_clone_v4/web_dynamic/static/;
        try_files \$uri \$uri/ =404;
    }
    location / {
        proxy_pass http://0.0.0.0:5003;
      }
    location /airbnb-onepage {
        proxy_pass http://0.0.0.0:5000/airbnb-onepage;
    }
    location ~ ^/airbnb-dynamic/number_odd_or_even/([0-9]+)$ {
        proxy_pass http://0.0.0.0:5001/number_odd_or_even/\$1;
    }
    location /api/ {
        proxy_pass http://0.0.0.0:5002;
    }
    if (\$request_filename ~ redirect_me){
        rewrite ^ https://highrate01/ permanent;
    }
    error_page 404 /error_404.html;
    location = /error_404.html {
        internal;
    }
}
EOF

# Restart Nginx to apply the changes
sudo systemctl restart nginx
echo "Nginx configuration has been successfully updated."

# Setup tmux session for task 4
cd /home/ubuntu/AirBnB_clone_v3
tmux new-session -d 'gunicorn --bind 0.0.0.0:5002 api.v1.app:app'

# Setup tmux session for task 5
cd /home/ubuntu/AirBnB_clone_v4

echo "Script execution completed successfully!"
