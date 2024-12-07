# Deployment Guide - AWS EC2

This guide explains how to deploy the Job Portal application to AWS EC2 using Terraform and Docker.

## Prerequisites

1. AWS Account with appropriate permissions
2. AWS CLI installed and configured
3. Terraform installed
4. Docker and Docker Compose installed
5. SSH key pair for EC2 access

## Step-by-Step Deployment Process

### 1. AWS Configuration

1. Create an AWS account if you don't have one
2. Create an IAM user with appropriate permissions
3. Configure AWS CLI with your credentials:
```bash
aws configure
```

### 2. Create SSH Key Pair

1. Go to AWS Console > EC2 > Key Pairs
2. Create a new key pair named "jobportal-key"
3. Download the .pem file
4. Move it to your project root directory
5. Set proper permissions:
```bash
chmod 400 jobportal-key.pem
```

### 3. Initialize Terraform

```bash
cd terraform
terraform init
```

### 4. Apply Terraform Configuration

```bash
terraform plan    # Review the changes
terraform apply   # Apply the changes
```

### 5. Deploy the Application

```bash
# Make deployment script executable
chmod +x scripts/deploy_ec2.sh

# Run deployment script
./scripts/deploy_ec2.sh
```

### 6. Verify Deployment

1. Get the EC2 public IP:
```bash
cd terraform
terraform output public_ip
```

2. Access the application:
- Frontend: http://<EC2_PUBLIC_IP>:3000
- Backend: http://<EC2_PUBLIC_IP>:8000
- Health Check: http://<EC2_PUBLIC_IP>:8000/health/

## Monitoring and Maintenance

### View Logs
```bash
# SSH into EC2
ssh -i "jobportal-key.pem" ubuntu@<EC2_PUBLIC_IP>

# View Docker logs
cd /app
docker-compose logs -f
```

### Update Application
To deploy updates:
1. Make your changes locally
2. Run the deployment script again:
```bash
./scripts/deploy_ec2.sh
```

### Troubleshooting

1. Check EC2 instance status in AWS Console
2. View Docker container logs:
```bash
ssh -i "jobportal-key.pem" ubuntu@<EC2_PUBLIC_IP>
cd /app
docker-compose ps
docker-compose logs
```

3. Check security group settings in AWS Console

### Cleanup

To destroy the infrastructure:
```bash
cd terraform
terraform destroy
```

## Security Notes

1. In production:
   - Restrict SSH access to your IP in security group
   - Use HTTPS with SSL certificate
   - Set up proper monitoring and logging
   - Use strong passwords and secure key management

2. Environment Variables:
   - Never commit .env file to version control
   - Use AWS Secrets Manager for sensitive data in production

## Backup and Restore

### Create Backup
```bash
ssh -i "jobportal-key.pem" ubuntu@<EC2_PUBLIC_IP>
cd /app
docker-compose exec backend python manage.py dumpdata > backup.json
```

### Restore from Backup
```bash
scp -i "jobportal-key.pem" backup.json ubuntu@<EC2_PUBLIC_IP>:/app/
ssh -i "jobportal-key.pem" ubuntu@<EC2_PUBLIC_IP>
cd /app
docker-compose exec backend python manage.py loaddata backup.json
