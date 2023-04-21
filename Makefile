
generate_migration:
	alembic revision --autogenerate -m "$(NAME)"


migrate:
	alembic upgrade head
