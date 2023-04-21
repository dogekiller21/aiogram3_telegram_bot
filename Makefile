
generate_migration:
	alembic revision --autogenerate -m "$(NAME)"


migrate:
	alembic upgrade head

run_bot:
	poetry run python __main__.py
