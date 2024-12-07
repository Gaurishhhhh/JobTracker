#!/bin/bash
cd /home/ec2-user/jobportal

# Start application using docker-compose
docker-compose up -d

# Health check
sleep 30
curl http://localhost:8000/health
