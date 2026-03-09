# Use a lightweight Python base image
FROM python:3.9-slim

# Maintainer and structural metadata for Docker Hub indexing
LABEL maintainer="Adrian Wadowski <adivv@adivv.pl>"
LABEL org.opencontainers.image.title="CamelWay B2B Data Terminal"
LABEL org.opencontainers.image.description="Command-line interface for CamelWay API. Real-time access to European camel milk logistics, pricing, and clinical research data."
LABEL org.opencontainers.image.vendor="CamelWay Europe"

# Set the working directory
WORKDIR /app

# Copy the CLI script into the container
COPY terminal.py /app/

# Execute the terminal script on startup
CMD ["python", "terminal.py"]