# Job Portal Application - Docker Setup Guide

## Prerequisites

1. Install Docker Desktop for Windows
2. Install Git
3. Make sure ports 8000 and 3000 are available on your machine

## Step-by-Step Setup Guide

### 1. Configure Environment Variables

1. Open the `.env` file in the root directory
2. Update the following variables with your values:
```
DJANGO_SECRET_KEY=your-secret-key-here
DB_PASSWORD=your-secure-password
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
```

### 2. Build and Start the Application

There are two ways to start the application:

#### Option 1: Using the start script (Recommended)

```bash
# Make scripts executable (if not already)
chmod +x scripts/*.sh

# Start the application
./scripts/start_containers.sh
```

#### Option 2: Using Docker Compose directly

```bash
# Build the images
docker-compose build

# Start the containers
docker-compose up -d
```

### 3. Verify the Setup

1. Check if containers are running:
```bash
docker-compose ps
```

2. Check container logs:
```bash
docker-compose logs
```

3. Access the applications:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Admin Interface: http://localhost:8000/admin

### 4. Common Commands

```bash
# Stop the application
docker-compose down

# View logs
docker-compose logs -f

# Rebuild and restart containers
docker-compose up -d --build

# Check container health
docker-compose ps

# Access container shell
docker-compose exec backend bash
docker-compose exec frontend sh
```

### 5. Troubleshooting

If you encounter issues:

1. Check the logs:
```bash
docker-compose logs
```

2. Verify environment variables:
```bash
./scripts/check_env.sh
```

3. Restart the containers:
```bash
docker-compose down
./scripts/start_containers.sh
```

4. Clean up and rebuild:
```bash
# Stop and remove containers
docker-compose down

# Remove all images
docker-compose down --rmi all

# Remove volumes
docker-compose down -v

# Rebuild and start
./scripts/start_containers.sh
```

## Directory Structure

```
.
├── Dockerfile              # Backend Dockerfile
├── Dockerfile.frontend     # Frontend Dockerfile
├── docker-compose.yml      # Docker Compose configuration
├── .env                    # Environment variables
├── .dockerignore          # Docker ignore file
└── scripts/
    ├── check_env.sh       # Environment variables checker
    └── start_containers.sh # Container startup script
```

## Health Checks

- Backend health check: http://localhost:8000/health/
- Frontend health check: http://localhost:3000/

## Monitoring

You can monitor the health of your containers using:

```bash
# View container status
docker-compose ps

# View container metrics
docker stats
```

## Backup and Restore

### Create a backup

```bash
# Backup the database
docker-compose exec backend python manage.py dumpdata > backup.json
```

### Restore from backup

```bash
# Restore the database
docker-compose exec backend python manage.py loaddata backup.json
```

## Security Notes

1. Never commit the `.env` file to version control
2. Regularly update your Docker images
3. Use strong passwords in your environment variables
4. Keep your Docker Engine and Docker Compose up to date

## Next Steps

After successfully running the application, you can:

1. Set up CI/CD pipeline
2. Configure AWS infrastructure
3. Implement SonarQube for code quality analysis
