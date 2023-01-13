# docker/backend/Dockerfile
FROM python:3.8

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./backend/requirements.txt /app/backend/

RUN pip install --upgrade pip && \
    pip install -r backend/requirements.txt

# COPY ./docker /app/docker
COPY ./ /app/backend

EXPOSE 8000