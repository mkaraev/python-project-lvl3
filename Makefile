install:
	poetry install

test:
	poetry run pytest tests --cov=page_loader

lint:
	poetry run flake8 page_loader

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build