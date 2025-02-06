server {
    listen 80;

    location /rota1 {
        proxy_pass http://app-service:5000/health;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}