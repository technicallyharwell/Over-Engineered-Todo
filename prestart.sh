#!/usr/bin/env bash

# Let the DB start
python ./app/backend_pre_start.py
#python ./app/postgres_pre_start.py

echo "Waiting for postgres..."
sleep 5;

# Run migrations
echo "Running migrations..."
alembic upgrade head

echo "starting server..."
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
# Create initial data in DB
#python ./app/initial_data.py
