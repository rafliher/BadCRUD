server {
    listen 80;

    location / {
        proxy_pass http://selenium-hub:4444;
    }

    location /wd/hub/ {
        proxy_pass http://selenium-hub:4444;
        proxy_set_header X-Content-Type-Options nosniff;
        proxy_set_header X-XSS-Protection "1; mode=block";
        proxy_hide_header Content-Security-Policy;
    }

    location /styles/ {
        alias /usr/share/nginx/html/styles/;
    }

    add_header X-Frame-Options "SAMEORIGIN";
}
