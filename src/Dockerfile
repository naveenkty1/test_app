FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev python-flask


WORKDIR /opt/app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "/app/app.py" ]
