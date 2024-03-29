install:
	poetry install

test:
	poetry run pytest tests --cov=page_loader

lint:
	poetry run flake8 page_loader
	poetry run flake8 tests
	poetry run isort page_loader
	poetry run isort tests

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build