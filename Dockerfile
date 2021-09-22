FROM tiangolo/uvicorn-gunicorn:python3.8-slim

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./app /app