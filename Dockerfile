FROM python:3.10

ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./django_project /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
