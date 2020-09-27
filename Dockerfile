FROM python:3.7-alpine

ENV PYTHONBUFFERED=1
ENV DEBUG=0
ENV DJANGO_SETTINGS_MODULE=conduit.settings

RUN mkdir /code
RUN apk add build-base
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN python manage.py collectstatic --no-input --dry-run

CMD gunicorn conduit.wsgi --bind 0.0.0.0:8000
