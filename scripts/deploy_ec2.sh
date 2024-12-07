#!/bin/bash

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo "AWS CLI is not installed. Please install it first."
    exit 1
fi

# Check if required environment variables are set
if [ -z "$AWS_ACCESS_KEY_ID" ] || [ -z "$AWS_SECRET_ACCESS_KEY" ]; then
    echo "AWS credentials are not set. Please set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY."
    exit 1
fi

# Get the EC2 instance public IP from Terraform output
EC2_IP=$(terraform -chdir=terraform output -raw public_ip)

if [ -z "$EC2_IP" ]; then
    echo "Could not get EC2 IP address. Make sure Terraform has been applied successfully."
    exit 1
fi

echo "Deploying to EC2 instance at $EC2_IP..."

# Build Docker images
echo "Building Docker images..."
docker-compose build

# Save images to tar files
echo "Saving Docker images..."
docker save jobportal-backend:latest > backend.tar
docker save jobportal-frontend:latest > frontend.tar

# Copy files to EC2
echo "Copying files to EC2..."
scp -i "jobportal-key.pem" \
    backend.tar \
    frontend.tar \
    docker-compose.yml \
    .env \
    scripts/start_containers.sh \
    scripts/check_env.sh \
    ubuntu@$EC2_IP:/app/

# Clean up local tar files
rm backend.tar frontend.tar

# SSH into EC2 and deploy
echo "Deploying on EC2..."
ssh -i "jobportal-key.pem" ubuntu@$EC2_IP << 'EOF'
    cd /app
    
    # Load Docker images
    docker load < backend.tar
    docker load < frontend.tar
    rm backend.tar frontend.tar

    # Make scripts executable
    chmod +x scripts/*.sh

    # Start containers
    ./scripts/start_containers.sh

    # Clean up
    docker system prune -f
EOF

echo "Deployment completed successfully!"
echo "Application is accessible at: http://$EC2_IP"
