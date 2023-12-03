# syntax=docker/dockerfile:1
FROM python:3.11.0-alpine
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/cache/apk/*
COPY . .
CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0"]
