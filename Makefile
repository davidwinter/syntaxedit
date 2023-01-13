setup:
	poetry install
	poetry run pre-commit install

lint:
	poetry run pre-commit run --all-files

test:
	poetry run pytest

example:
	poetry run python example.py

.PHONY: setup lint test example
