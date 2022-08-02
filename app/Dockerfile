FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update -y 
RUN apt-get install -y libsasl2-dev \
        python-dev libldap2-dev \
        libssl-dev python3-dev \
        default-libmysqlclient-dev build-essential

RUN apt-get clean -y

RUN pip install --upgrade pip
RUN pip install -r requirements.txt