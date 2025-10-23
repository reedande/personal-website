FROM python:3.11-slim

# set environment
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=app.py \
    FLASK_ENV=production \
    PORT=5000

WORKDIR /app

# system deps for some wheels and sqlite
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

# create a non-root user
RUN adduser --disabled-password --gecos '' appuser

# copy requirements first for better caching
COPY requirements.txt /app/requirements.txt

# install python deps
RUN python -m pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r /app/requirements.txt

# copy application code
COPY . /app

# ensure DB file directory exists and set correct perms
RUN mkdir -p /app && chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

# Run with gunicorn for production; bind to 0.0.0.0:5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
