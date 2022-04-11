# syntax=docker/dockerfile:1

FROM python:3.10.2-slim-bullseye

WORKDIR /app

COPY . .
EXPOSE 1883

RUN pip3 install -r requirements.txt
CMD [ "python3", "laptop.py" ]