@echo off
echo Verifying AWS Configuration...
echo.

echo Checking AWS CLI installation...
aws --version
if %ERRORLEVEL% NEQ 0 (
    echo AWS CLI is not installed or not in PATH
    echo Please install AWS CLI first
    exit /b 1
)
echo AWS CLI is installed
echo.

echo Checking AWS credentials...
aws sts get-caller-identity
if %ERRORLEVEL% NEQ 0 (
    echo AWS credentials are not configured properly
    echo Please run 'aws configure' and set up your credentials
    exit /b 1
)
echo AWS credentials are configured properly
echo.

echo Checking AWS region...
aws configure get region
if %ERRORLEVEL% NEQ 0 (
    echo AWS region is not configured
    echo Please run 'aws configure' and set up your region
    exit /b 1
)
echo AWS region is configured
echo.

echo All checks passed! Your AWS configuration is ready.
