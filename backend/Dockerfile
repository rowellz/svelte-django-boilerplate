# docker/backend/Dockerfile
FROM python:3.8

RUN apt-get update

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./backend/requirements.txt /app/backend/

RUN pip install --upgrade pip && \
    pip install -r backend/requirements.txt

EXPOSE 8000