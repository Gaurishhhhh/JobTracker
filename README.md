# Job Portal Application

A dynamic web-based job portal application built with Django that connects job seekers with recruiters. The application provides a platform for recruiters to post jobs and manage applications, while job seekers can search for opportunities and apply to positions.

## Features

### For Job Seekers
- User registration and profile management
- Resume upload functionality
- Browse available job listings
- Apply to jobs with cover letters
- Track application status
- View job details and company information

### For Recruiters
- Company profile management
- Post job opportunities
- Manage job applications
- Accept/Reject candidates
- Close job positions
- View applicant details and resumes

## Technology Stack

- **Backend**: Django 3.2.25
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite3
- **Additional Libraries**: 
  - django-crispy-forms
  - crispy-bootstrap4

## Project Structure

```
project_root/
├── db.sqlite3          # SQLite database file
├── manage.py           # Django management script
├── media/             # Uploaded files (resumes)
├── static/            # Static files (CSS, images)
├── task_manager/      # Project configuration
├── tasks/             # Main application
└── templates/         # HTML templates
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser (Admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   - Main site: http://127.0.0.1:8000
   - Admin interface: http://127.0.0.1:8000/admin

## Usage Guide

### For Job Seekers

1. **Registration**
   - Click "Register" in the navigation bar
   - Select "As Job Seeker"
   - Fill in your details and upload your resume

2. **Applying for Jobs**
   - Browse available positions on the home page
   - Click "View Details" on any job listing
   - Click "Apply Now" and submit your application with a cover letter

3. **Managing Applications**
   - Track your application status
   - View job details and company information

### For Recruiters

1. **Registration**
   - Click "Register" in the navigation bar
   - Select "As Recruiter"
   - Fill in your company details

2. **Posting Jobs**
   - Click "Post Job" in the navigation bar
   - Fill in the job details including:
     - Title
     - Description
     - Requirements
     - Location
     - Salary

3. **Managing Applications**
   - Access "Applications" in the navigation bar
   - View applicant details and resumes
   - Accept or reject applications
   - Close positions when filled

### Admin Interface

1. **Accessing Admin Panel**
   - Go to http://127.0.0.1:8000/admin
   - Login with superuser credentials

2. **Managing Data**
   - Access and modify all database records
   - Manage users, jobs, and applications
   - Monitor system activity

## Database Schema

### User Models
- **JobSeeker**
  - User (OneToOne)
  - Phone
  - Resume
  - Skills
  - Experience

- **Recruiter**
  - User (OneToOne)
  - Company Name
  - Company Description

### Job Models
- **Job**
  - Title
  - Company (ForeignKey to Recruiter)
  - Description
  - Requirements
  - Location
  - Salary
  - Status
  - Created/Updated timestamps

- **JobApplication**
  - Job (ForeignKey)
  - Applicant (ForeignKey to JobSeeker)
  - Cover Letter
  - Status
  - Applied/Updated timestamps

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please create an issue in the repository or contact the development team.
