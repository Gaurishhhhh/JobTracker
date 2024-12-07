#!/bin/bash

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "Docker is not running. Please start Docker first."
    exit 1
fi

# Check environment variables
if ! ./scripts/check_env.sh; then
    echo "Environment check failed. Please set all required variables in .env file."
    exit 1
fi

# Build and start containers
echo "Building and starting containers..."
docker-compose build --no-cache
docker-compose up -d

# Wait for services to be healthy
echo "Waiting for services to be healthy..."
timeout=300
elapsed=0
interval=10

while [ $elapsed -lt $timeout ]; do
    if docker-compose ps | grep -q "healthy"; then
        echo "All services are healthy!"
        exit 0
    fi
    
    echo "Waiting for services to become healthy... ($elapsed/$timeout seconds)"
    sleep $interval
    elapsed=$((elapsed + interval))
done

echo "Timeout waiting for services to become healthy"
docker-compose logs
exit 1
