#!/usr/bin/env bash

cp ./alembic.ini ./tests/config/alembic.ini
cp -r ./alembic ./tests/config/alembic

cd ./tests/config && poetry run alembic upgrade head

cd ../../
poetry run coverage run -m pytest
test_result=$?
poetry run coverage xml

# cleanup..
cd ./tests/config
rm -rf ./alembic
rm ./alembic.ini
rm ./test.db

echo "Test result: $test_result"
exit $test_result
