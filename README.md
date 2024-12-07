# Job Portal

A Django-based job portal application with features for job seekers and recruiters.

## Features

- Job Seeker Features:
  - Resume upload and management
  - Job application with cover letters
  - Profile management
  
- Recruiter Features:
  - Post job listings
  - Manage applications (Accept/Reject)
  - Remove job postings
  - View resumes and cover letters

## Deployment to AWS Elastic Beanstalk via Cloud9

1. Set up Cloud9 Environment:
   ```bash
   # Clone the repository
   git clone https://github.com/ChethanNCI/JobTracker.git
   cd JobTracker

   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt
   ```

2. Initialize Elastic Beanstalk:
   ```bash
   # Install EB CLI
   pip install awsebcli

   # Initialize EB application
   eb init -p python-3.11 jobportal

   # Create environment
   eb create jobportal-env
   ```

3. Configure Environment Variables:
   - Go to Elastic Beanstalk Console
   - Navigate to Configuration
   - Add environment variables:
     - SECRET_KEY
     - DEBUG
     - ALLOWED_HOSTS
     - DATABASE_URL (if using RDS)

4. Deploy:
   ```bash
   eb deploy
   ```

5. Open the application:
   ```bash
   eb open
   ```

## Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/ChethanNCI/JobTracker.git
   cd JobTracker
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

- `task_manager/` - Main project directory
  - `settings.py` - Project settings
  - `urls.py` - Main URL configuration
  
- `tasks/` - Main application directory
  - `views.py` - Application views
  - `models.py` - Database models
  - `forms.py` - Forms
  - `urls.py` - Application URLs

- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)
- `media/` - User uploaded files
- `.ebextensions/` - Elastic Beanstalk configuration

## Contributing

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit:
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

3. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Create a Pull Request

## License

This project is licensed under the MIT License.
