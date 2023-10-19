FROM python:3.11 as py-base

# https://python-poetry.org/docs#ci-recommendations
ENV POETRY_VERSION=1.5.1
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv

# Tell Poetry where to place its cache and virtual environment
ENV POETRY_CACHE_DIR=/opt/.cache

# Create stage for Poetry installation
FROM py-base as poetry-base

# Creating a virtual environment just for poetry and install it with pip
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install --upgrade setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Create new stage for the FastAPI application
FROM py-base as app-base

# Copy Poetry venv from the previous stage
COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}

# Update PATH and PYTHONPATH in application layer
ENV PATH="${PATH}:${POETRY_VENV}/bin"
ENV PYTHONPATH="${PYTHONPATH}:/api"

RUN chmod -R 777 /opt