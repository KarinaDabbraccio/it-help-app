FROM ubuntu:focal as internal

ARG DB_URL

ENV DB_URL=$DB_URL

RUN apt-get update

RUN yes | apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget ufw

WORKDIR /tmp

RUN wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz

RUN tar -xf Python-3.10.0.tgz

WORKDIR Python-3.10.0

RUN ./configure

RUN make install

WORKDIR /app

FROM internal as base

RUN yes | apt install python3-pip

RUN pip3 install django

RUN pip3 install psycopg2-binary django-dotenv tzdata

FROM base as development

RUN mkdir app/

COPY . app/

WORKDIR app

RUN python3 manage.py makemigrations src

RUN python3 manage.py sqlmigrate src 0001

RUN python3 manage.py migrate

FROM development as test

CMD ["python3", "manage.py", "test"]

FROM test as build

EXPOSE 5432 8000

RUN ufw allow 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
