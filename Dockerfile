
# ---------------------------------------------------------------------------
# Project: 🛡️ Neural Gate v3.1 — AI Crowd Intelligence & Autonomous Incident Capture
# File:    Dockerfile
# Author:  AHMED ZARAI
# ---------------------------------------------------------------------------

FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for OpenCV/AI
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set the environment switch
ENV RUNNING_IN_DOCKER=true

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]