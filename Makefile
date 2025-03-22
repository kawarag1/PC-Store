deploy:
	docker-compose --env-file .env -f docker-compose.backend.yml --project-directory . up --build -d

build:
	docker-compose --env-file .env -f docker-compose.backend.yml --project-directory . up --build -d
