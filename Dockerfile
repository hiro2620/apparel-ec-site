FROM python:3.10

ENV PYTHONUNBUFFERED 1
RUN mkdir /workspace
WORKDIR /workspace
RUN apt-get update && apt-get -y install default-mysql-client
COPY requirements.txt /workspace/
RUN pip install --upgrade pip && pip install --requirement requirements.txt
COPY . /workspace/