FROM python:3.12

RUN apt-get update && apt-get install -y build-essential python3-dev libgmp3-dev

RUN pip install --upgrade pip
RUN pip install pipenv

WORKDIR ~/

COPY Pipfile* ./

RUN pipenv install --dev --system
