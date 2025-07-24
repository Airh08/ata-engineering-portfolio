# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip

# Copy requirements file
COPY ./requirements.txt .

## Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy wait_for_it.sh script
COPY ./docker/wait_for_it.sh /wait_for_it.sh
RUN chmod +x /wait_for_it.sh


## Copy project files
COPY . .

