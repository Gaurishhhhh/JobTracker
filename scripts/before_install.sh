#!/bin/bash
# Install dependencies
yum update -y
yum install -y docker
service docker start
usermod -a -G docker ec2-user

# Install docker-compose
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Clean up
rm -rf /home/ec2-user/jobportal
mkdir -p /home/ec2-user/jobportal
