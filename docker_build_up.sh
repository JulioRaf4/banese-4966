# comando para subir todos os container
docker compose build
docker compose up -d

# comando para ver todos os container
docker compose ps -a

# Stop development environment
docker-compose down

# Rebuild and restart services while preserving volumes (useful for code changes)
docker-compose up -d --build