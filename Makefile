setup:
	poetry install

test:
	poetry run pytest

example:
	poetry run python example.py

.PHONY: setup test example
