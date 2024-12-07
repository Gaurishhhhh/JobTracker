#!/bin/bash

# Required environment variables
REQUIRED_VARS=(
    "DJANGO_SETTINGS_MODULE"
    "DJANGO_SECRET_KEY"
    "DEBUG"
    "ALLOWED_HOSTS"
    "DB_NAME"
    "DB_USER"
    "DB_PASSWORD"
    "DB_HOST"
    "DB_PORT"
)

# Check each required variable
for VAR in "${REQUIRED_VARS[@]}"
do
    if [[ -z "${!VAR}" ]]; then
        echo "Error: Required environment variable $VAR is not set."
        exit 1
    fi
done

echo "All required environment variables are set."
exit 0
