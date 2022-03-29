FROM openjdk:slim

copy --from=python:3.8.10 / /

RUN apt-get update

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000
COPY init.sh /usr/local/bin/

RUN chmod +x  /usr/local/bin/init.sh
ENTRYPOINT  ["init.sh"]
