FROM python:3.9-slim

WORKDIR /app

COPY .env .env

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]