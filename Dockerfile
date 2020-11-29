FROM python:3.8
MAINTAINER Anderson Foschiera

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /www

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD . .
