# orm-todo

## Quickstart
- `pip install poetry`
- `poetry install`
- `poetry run prestart.sh`
  - validate that the db `test.db` was created
- 

## Alembic usage
- Run `alembic upgrade head` to upgrade to the latest migration.
- Run `alembic revision --autogenerate -m "message"` to generate a new migration.
- Run `alembic downgrade -1` to downgrade the database by one migration.

## DB Helpers
- `backend_pre_start.py` creates a db session and executes `SELECT 1` to validate connection
- `initial_data.py` uses `init_db.py` to create the db and then populates it with initial data
