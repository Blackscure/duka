# Use an official Python image
FROM python:3.13-slim

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# working directory inside container
WORKDIR /app

# system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into container
COPY . /app/

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
