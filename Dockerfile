FROM python:3.7-alpine

EXPOSE 80

RUN set -ex && mkdir /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN set -ex && pip3 install -r requirements.txt

COPY . /usr/src/app

CMD /usr/src/app/server.py
