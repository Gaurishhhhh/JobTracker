# Job Portal Application

A dynamic web-based job portal application built with Django that connects job seekers with recruiters. This application facilitates job postings, applications, and hiring processes.

## Features

### For Job Seekers
- User registration with profile management
- Resume upload functionality
- Browse and search job listings
- Apply to jobs with cover letters
- Track application status
- View company details

### For Recruiters
- Company profile management
- Post and manage job listings
- Review applications and resumes
- Accept/Reject candidates
- Close positions when filled
- Track hiring progress

## Project Structure
```
project_root/
├── task_manager/        # Project configuration
├── tasks/              # Main application
│   ├── models.py       # Database models
│   ├── views.py        # View logic
│   ├── forms.py        # Form definitions
│   └── admin.py        # Admin interface
├── templates/          # HTML templates
├── static/             # Static files (CSS, JS)
├── media/             # User uploads
└── manage.py          # Django CLI
```

## Setup Instructions

1. **Clone Repository**
```bash
git clone https://github.com/Gaurishhhhh/JobTracker.git
cd JobTracker
```

2. **Create Virtual Environment**
```bash
python -m venv venv
```

3. **Activate Environment**
```bash
# Windows
.\venv\Scripts\activate

# Unix/MacOS
source venv/bin/activate
```

4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

5. **Database Setup**
The project uses SQLite database which will be created automatically when you run migrations. Follow these steps:

```bash
# Create database tables
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create admin superuser
python manage.py createsuperuser
# Follow prompts to create username and password
```

The above commands will:
- Create a new SQLite database file (db.sqlite3)
- Set up all required database tables
- Create necessary relationships between tables
- Create an admin user for accessing the admin interface

Important Database Models:
- Users (Django's built-in user model)
- JobSeeker (Profile information and resume storage)
- Recruiter (Company information)
- Job (Job listings)
- JobApplication (Application tracking)

6. **Media Files Setup**
Create a directory for uploaded files:
```bash
# Windows
mkdir media
mkdir media\resumes

# Unix/MacOS
mkdir -p media/resumes
```

7. **Run Server**
```bash
python manage.py runserver
```

## Accessing the Application

1. **Admin Interface**
```
URL: http://127.0.0.1:8000/admin
Login with superuser credentials created during setup
```

2. **Main Application**
```
URL: http://127.0.0.1:8000
```

## Usage Guide

### Job Seekers
1. Register as a job seeker
2. Complete your profile and upload resume
3. Browse available positions
4. Apply with cover letters
5. Track your applications

### Recruiters
1. Register as a recruiter
2. Create company profile
3. Post job opportunities
4. Review applications
5. Manage hiring process

## Technology Stack
- **Backend**: Django 3.2.25
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Database**: SQLite3
- **Additional**: 
  - django-crispy-forms
  - crispy-bootstrap4

## Database Schema

### User Models
```python
# JobSeeker Model
- user (OneToOneField to User)
- phone (CharField)
- resume (FileField)
- skills (TextField)
- experience (IntegerField)

# Recruiter Model
- user (OneToOneField to User)
- company_name (CharField)
- company_description (TextField)

# Job Model
- title (CharField)
- company (ForeignKey to Recruiter)
- description (TextField)
- requirements (TextField)
- location (CharField)
- salary (CharField)
- status (CharField with choices)
- created_at (DateTimeField)
- updated_at (DateTimeField)

# JobApplication Model
- job (ForeignKey to Job)
- applicant (ForeignKey to JobSeeker)
- cover_letter (TextField)
- status (CharField with choices)
- applied_at (DateTimeField)
- updated_at (DateTimeField)
```

## Troubleshooting

1. **Database Issues**
If you encounter database issues:
```bash
# Remove existing database
rm db.sqlite3

# Remove migration files
rm -rf tasks/migrations/

# Recreate database
python manage.py makemigrations tasks
python manage.py migrate
```

2. **Media Files**
If uploaded files are not visible:
- Ensure media directory exists
- Check permissions on media directory
- Verify MEDIA_URL and MEDIA_ROOT in settings.py

## Contributing
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License
MIT License
