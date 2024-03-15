docker network create cybellum-network
docker volume create cybellum_pg-data
docker compose build
docker compose up -d