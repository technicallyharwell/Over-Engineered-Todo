#! /usr/bin/env bash

cp ./alembic.ini ./tests/config/alembic.ini
cp -r ./alembic ./tests/config/alembic

cd ./tests/config && alembic upgrade head

# @as_declarative decorator was deprecated with SQLAlchemy 2.0 release
# TODO - refactor SQLA usage to be compatible with 2.0
export SQLALCHEMY_SILENCE_UBER_WARNING=1

poetry run pytest

# cleanup
rm -rf ./alembic
rm ./alembic.ini
rm ./test.db
