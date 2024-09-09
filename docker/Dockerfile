FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./base.txt /code/base.txt

RUN pip install --upgrade pip
RUN pip install -r /code/base.txt

COPY . /code/
WORKDIR /code

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
