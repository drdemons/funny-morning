# syntax = docker/dockerfile:1.2
FROM python:3.9-alpine
ADD . /code
WORKDIR /code
COPY requirements.txt requirements.txt
RUN apk add --update --no-cache g++ gcc libxslt-dev
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py", "--log=INFO"]
