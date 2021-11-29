FROM tiangolo/uvicorn-gunicorn:python3.8-slim

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./app /app