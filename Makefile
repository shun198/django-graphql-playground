CONTAINER_NAME = app
RUN_APP = docker-compose exec $(CONTAINER_NAME)
RUN_POETRY =  $(RUN_APP) poetry run
RUN_DJANGO = $(RUN_POETRY) python manage.py
RUN_PYTEST = $(RUN_POETRY) pytest
RUN_TERRAFORM = docker-compose -f infra/docker-compose.yml run --rm terraform

prepare:
	npm install
	docker-compose up -d --build

up:
	docker-compose up -d

build:
	docker-compose build

install:
	npm install $(FRONTEND_PATH)

down:
	docker-compose down

loaddata:
	$(RUN_DJANGO) loaddata fixture.json

makemigrations:
	$(RUN_DJANGO) makemigrations

migrate:
	$(RUN_DJANGO) migrate

show_urls:
	$(RUN_DJANGO) show_urls

shell:
	$(RUN_DJANGO) debugsqlshell

superuser:
	$(RUN_DJANGO) createsuperuser

test:
	$(RUN_PYTEST)

format:
	$(RUN_POETRY) black .
	$(RUN_POETRY) isort .

db:
	docker exec -it db bash

collectstatic:
	$(RUN_DJANGO) collectstatic

init:
	$(RUN_TERRAFORM) init

fmt:
	$(RUN_TERRAFORM) fmt

validate:
	$(RUN_TERRAFORM) validate

show:
	$(RUN_TERRAFORM) show

apply:
	$(RUN_TERRAFORM) apply -auto-approve

destroy:
	$(RUN_TERRAFORM) destroy