FROM python:3-alpine
LABEL maintainer="sopra <sopraneeno@gmail.com>"

RUN [ "apk", "add", "--no-cache", "git", "libxml2", "libxml2-dev", "gcc", "g++", "libxslt", "libxslt-dev" ]
RUN [ "pip", "install", "requests", "beautifulsoup4", "lxml" ]

ADD . /app

CMD [ "/bin/bash" ]
