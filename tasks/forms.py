from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import JobSeeker, JobApplication, Job, Recruiter

class JobSeekerRegistrationForm(UserCreationForm):
    phone = forms.CharField(max_length=15)
    resume = forms.FileField()
    skills = forms.CharField(widget=forms.Textarea)
    experience = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RecruiterRegistrationForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)
    company_description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 4}),
        }

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'requirements', 'location', 'salary']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'requirements': forms.Textarea(attrs={'rows': 4}),
        }

class ResumeUpdateForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ['resume']
        widgets = {
            'resume': forms.FileInput(attrs={'class': 'form-control'})
        }
