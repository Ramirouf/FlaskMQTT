FROM python:3.11-slim

WORKDIR /app

RUN apt-get -y update
RUN apt-get install python3-dev build-essential pkg-config -y

ENV TZ="America/Argentina/Buenos_Aires"

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["gunicorn", "-w", "4", "-b", ":8000", "app:app"]