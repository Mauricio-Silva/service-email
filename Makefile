#!make
include .env


dev-run:
	uvicorn app.main:app

dev-reload:
	uvicorn app.main:app --reload

prod-run:
	uvicorn app.main:app --host 0.0.0.0 --port ${APP_PORT}

prod-reload:
	uvicorn app.main:app --reload --host 0.0.0.0 --port ${APP_PORT}
