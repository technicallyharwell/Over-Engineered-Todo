# Over-engineered Todo API ft. FastAPI
A fully featured twist on the classic REST API To-do list application, showcasing modern Python application development 
best practices and packages.

## Features

### FastAPI
FastAPI is used to implement the REST API backend, which is a modern Python framework that is built on top of Starlette.

In addition to the ASGI performance benefits provided by Starlette, FastAPI has a very powerful dependency injection
system that greatly simplifies the implementation of common patterns such as database sessions and authentication.

FastAPI also provides support for automatic OpenAPI document generation out of the box - no more manually creating
Swagger manifests!

### SQLAlchemy
SQLAlchemy is used to implement the ORM layer

### Alembic
Alembic is used to manage database migrations

### Pydantic
Pydantic is used to implement data models and schemas, which are used for request/response validation and serialization.

### Docker
Docker is used to containerize the application, and a multi-stage build is used to cache mostly-static layers such as
Poetry environment configuration.

### Jira
Development activities are planned and tracked with Jira, starting with high-level epics
which are broken down to user stories and tasks. Work is organized into sprints, where the tasks of each sprint are
pulled from a backlog. 

Jira automation is utilized for:
- Populating description fields of newly created tickets
- Automatically assigning tickets when the state is transitioned
- Populating Confluence pages when each sprint ends, and when an epic is completed

Additionally, Jira integrations with GitHub and Jenkins are used to track branches, commits,
and build status.

### Jenkins
Jenkins is used for CI/CD, with a multibranch pipeline approach that builds and tests each branch and PR.
CI stages include package installation, linting, testing, and code scanning, driven by containerized agents
which have a minimal set of dependencies required for each stage.

#### Package Management - Poetry
Package management is handled by Poetry, which is used to manage dependency versioning and virtual environments.

Dependency groups are implemented to separate dev and prod dependencies, e.g. `[tool.poetry.group.test.dependencies]`,
allowing local development and CI to utilize packages such as `pytest`, while the production image only contains a 
minimal set of dependencies required to run the application.

#### Linting - Ruff
Linting is handled by Ruff, which is a wrapper around Flake8, Black, and isort. Ruff uses Rust under the hood and is
**ridiculously fast**. 

#### Testing - Pytest
Testing is handled by Pytest, which is used to run unit and integration tests. `coverage` is used to generate coverage
reports, which are uploaded to SonarQube for analysis during CI.

One of the biggest benefits to using Pytest compared to other testing frameworks is the ability to use fixtures, which
can be scoped to the module, class, or function level. See `tests/conftest.py` for examples.

#### Code Scanning - SonarQube
SonarQube is used to scan the codebase for bugs, vulnerabilities, and code smells. Each branch is analyzed during CI,
and a webhook is configured to pass/fail CI execution based on the results of the scan.

[//]: # (## Quickstart)

[//]: # (- `pip install poetry`)

[//]: # (- `poetry install`)

[//]: # (- `poetry run prestart.sh`)

[//]: # (  - validate that the db `test.db` was created)

[//]: # (- )

[//]: # ()
[//]: # (## Alembic usage)

[//]: # (- Run `alembic upgrade head` to upgrade to the latest migration.)

[//]: # (- Run `alembic revision --autogenerate -m "message"` to generate a new migration.)

[//]: # (- Run `alembic downgrade -1` to downgrade the database by one migration.)

[//]: # ()
[//]: # (## DB Helpers)

[//]: # (- `backend_pre_start.py` creates a db session and executes `SELECT 1` to validate connection)

[//]: # (- `initial_data.py` uses `init_db.py` to create the db and then populates it with initial data)

[//]: # ()
[//]: # (### For Containerizing:)

[//]: # (- `prestart.sh` is run before the app starts and creates the db, runs migrations, and populates it with initial data)

[//]: # (- `run.sh` is the entrypoint for the container and runs the app)

