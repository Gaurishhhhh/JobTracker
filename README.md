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
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create Admin User**
```bash
python manage.py createsuperuser
```

7. **Run Server**
```bash
python manage.py runserver
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

## Database Models

### User Models
- JobSeeker (Profile, Resume, Skills)
- Recruiter (Company Details)

### Core Models
- Job (Listings)
- JobApplication (Applications)

## Contributing
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License
MIT License
