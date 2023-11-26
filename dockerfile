FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1

run apt-get update \
 && apt-get install -y ffmpeg \
  && rm -rf /var/lib/apt/lists/*

RUN groupadd -r universal \
  && useradd -g universal -r -m universal 

USER universal

WORKDIR /app

COPY --chown=universal:universal  ./requirements.txt .

COPY --chown=universal:universal  . .

RUN pip install -r requirements.txt


