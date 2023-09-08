FROM python:3.10 as py-base

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
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Create new stage for the FastAPI application
FROM py-base as app-base

# Copy Poetry venv from the previous stage
COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}

# Update PATH and PYTHONPATH in application layer
ENV PATH="${PATH}:${POETRY_VENV}/bin"
ENV PYTHONPATH="${PYTHONPATH}:/api"

# Disable stdout buffering
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /api

# Install dependencies
COPY pyproject.toml poetry.lock ./

# Validate that the project can be built
RUN poetry check

# Install dependencies
RUN poetry install --no-interaction --no-cache

# Copy project files
COPY . /api

# Run prestart setups
RUN chmod +x ./prestart.sh && \
    poetry run ./prestart.sh

# Run the application - uncomment to run from dockerfile instead of compose
#EXPOSE 8001
#CMD ["poetry", "run", "./run.sh"]
