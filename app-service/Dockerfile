FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app-service.py app-service.py

ENV APP_PORT=5000

CMD ["python", "app-service.py"]