# AWS Credentials Setup Guide

## Step 1: Create an AWS Account

1. Go to [AWS Console](https://aws.amazon.com/)
2. Click "Create an AWS Account" button
3. Follow the registration process
   - Provide email address
   - Create AWS account name
   - Provide credit card information (required for verification)
   - Verify your phone number
   - Choose a support plan (Free tier is sufficient)

## Step 2: Create IAM User

1. Log in to [AWS Management Console](https://console.aws.amazon.com/)
2. Search for "IAM" in the search bar
3. Click on "Users" in the left sidebar
4. Click "Create user"
5. Follow these steps:
   
   a. Set user details:
   - Username: `jobportal-admin`
   - Check "Provide user access to the AWS Management Console"
   - Select "I want to create an IAM user"
   - Create a password
   
   b. Set permissions:
   - Click "Attach policies directly"
   - Search and select these policies:
     * AmazonEC2FullAccess
     * AmazonVPCFullAccess
     * AmazonS3FullAccess
   
   c. Review and create user

## Step 3: Create Access Keys

1. Go to IAM dashboard
2. Click on "Users"
3. Click on your new user (jobportal-admin)
4. Go to "Security credentials" tab
5. Scroll to "Access keys"
6. Click "Create access key"
7. Choose "Command Line Interface (CLI)"
8. Click "Next"
9. Click "Create access key"
10. **IMPORTANT**: Download the CSV file or copy both:
    - Access key ID
    - Secret access key
    
    ⚠️ This is the ONLY time you can view the secret key!

## Step 4: Install AWS CLI

### For Windows:
1. Download the AWS CLI MSI installer for Windows (64-bit):
   - Go to [AWS CLI Download Page](https://aws.amazon.com/cli/)
   - Click "Download AWS CLI"
   - Run the downloaded MSI installer
   - Follow installation prompts

2. Verify installation:
   - Open Command Prompt
   - Run:
   ```bash
   aws --version
   ```

### For macOS/Linux:
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

## Step 5: Configure AWS CLI

1. Open Command Prompt or Terminal
2. Run:
```bash
aws configure
```

3. Enter the following information when prompted:
```
AWS Access Key ID: [Enter your access key ID]
AWS Secret Access Key: [Enter your secret access key]
Default region name: us-west-2 (or your preferred region)
Default output format: json
```

## Step 6: Verify Configuration

1. Test your credentials:
```bash
aws sts get-caller-identity
```

2. You should see output like:
```json
{
    "UserId": "AIDAXXXXXXXXXXXXXXXXX",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/jobportal-admin"
}
```

## Common AWS Regions

Choose the region closest to your location:
- us-east-1 (N. Virginia)
- us-east-2 (Ohio)
- us-west-1 (N. California)
- us-west-2 (Oregon)
- eu-west-1 (Ireland)
- eu-central-1 (Frankfurt)
- ap-southeast-1 (Singapore)
- ap-southeast-2 (Sydney)

## Security Best Practices

1. Never share your AWS access keys
2. Don't commit AWS credentials to version control
3. Regularly rotate your access keys
4. Use MFA (Multi-Factor Authentication) for your AWS account
5. Follow the principle of least privilege when assigning permissions

## Troubleshooting

If you encounter issues:

1. Verify credentials file location:
   - Windows: `C:\Users\USERNAME\.aws\credentials`
   - Linux/macOS: `~/.aws/credentials`

2. Check region configuration:
   - Windows: `C:\Users\USERNAME\.aws\config`
   - Linux/macOS: `~/.aws/config`

3. Common errors:
   - "Invalid credentials": Double-check your access key and secret key
   - "Region not found": Verify your region name is correct
   - "Access denied": Check IAM user permissions

For additional help, visit [AWS CLI Documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
