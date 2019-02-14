FROM python:3.7-alpine

EXPOSE 80

RUN set -ex && pip install pipenv --upgrade
RUN set -ex && mkdir /usr/src/app

WORKDIR /usr/src/app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN set -ex && pipenv install --dev --deploy --system

COPY . /usr/src/app

CMD /usr/src/app/server.py
