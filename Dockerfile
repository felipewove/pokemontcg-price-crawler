FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
