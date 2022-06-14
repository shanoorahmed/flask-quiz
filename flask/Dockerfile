FROM --platform=linux/amd64 python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:8000 --workers 4 "maths.app:create_app()"