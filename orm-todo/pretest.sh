#! /usr/bin/env bash

cp ./alembic.ini ./tests/config/alembic.ini
cp -r ./alembic ./tests/config/alembic

cd ./tests/config && alembic upgrade head

# call tests
poetry run pytest --disable-warnings

# cleanup
rm -rf ./alembic
rm ./alembic.ini
rm ./test.db
