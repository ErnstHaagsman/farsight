FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip

EXPOSE 5000

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

ENV FLASK_APP=app.py

# Flask compatibility
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]