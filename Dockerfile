FROM python:3.8.1-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /opt/app
WORKDIR /opt/app

ADD requirements.txt /opt/app
RUN pip install -r requirements.txt

ADD . /opt/app

