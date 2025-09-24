# Use official Python image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y git espeak ffmpeg && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port
EXPOSE 7860

# Run the app
CMD ["python", "app.py"]
