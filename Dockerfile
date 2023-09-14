FROM python:3.11 as py-base

RUN pip install -U pip setuptools && \
    pip install poetry==1.5.1

