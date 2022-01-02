FROM python:3.10.1-slim

WORKDIR /app

COPY . .

CMD ["python", "very_simple.py"]