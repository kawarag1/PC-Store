deploy:
	docker-compose --env-file .env -f docker-compose.backend.yml --project-directory . up --build -d

build:
	docker-compose --env-file ./Backend/.env -f docker-compose.backend.yml --project-directory . up --build -d


kill:
	taskkill /f /im python.exe