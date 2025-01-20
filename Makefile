black:
	black src

isort:
	isort src

ruff-check:
	ruff check src

ruff-format:
	ruff check src --fix

format: isort black ruff-format

setup:
	pre-commit install --hook-type pre-commit --hook-type pre-push

up:
	docker compose up --remove-orphans --build \
		bot \
		postgresql

db_downgrade:
	alembic downgrade -1

db_migrate:
	alembic revision --autogenerate -m "Upgrade database tables"

db_upgrade:
	alembic upgrade head
