FROM python:3.10-slim-buster

RUN apt-get update \
    && apt-get install -y sqlite3 gcc netcat \
    && apt-get clean

COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "main.py" ]

