# Frontend Dockerfile - Production Ready
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy frontend files
COPY . .

# Expose port
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run dev server
CMD ["python", "dev_server.py"]
