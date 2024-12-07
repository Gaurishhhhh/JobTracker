#!/bin/bash

echo "Job Portal Application - Quick Start Script"
echo "----------------------------------------"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo "Error: Docker is not running. Please start Docker first."
    exit 1
fi

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Error: .env file not found. Please create .env file with required variables."
    exit 1
fi

# Make scripts executable
chmod +x scripts/*.sh

echo "Checking environment variables..."
if ! ./scripts/check_env.sh; then
    echo "Please update your .env file with the required variables."
    exit 1
fi

echo "Starting containers..."
if ! ./scripts/start_containers.sh; then
    echo "Error starting containers. Please check the logs above."
    exit 1
fi

echo "
----------------------------------------
🎉 Success! Your application is running.

📱 Access the application:
   Frontend: http://localhost:3000
   Backend API: http://localhost:8000
   Admin Interface: http://localhost:8000/admin

📝 Useful commands:
   - View logs: docker-compose logs -f
   - Stop application: docker-compose down
   - Restart application: ./scripts/start_containers.sh

📚 For more information, check the README.md file
----------------------------------------"
