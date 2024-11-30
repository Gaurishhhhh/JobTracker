from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.http import FileResponse, Http404
from django.conf import settings
import os
from .models import JobSeeker, Recruiter, Job, JobApplication
from .forms import (
    JobSeekerRegistrationForm,
    RecruiterRegistrationForm,
    JobForm,
    JobApplicationForm
)

def home(request):
    jobs = Job.objects.filter(status='open').order_by('-created_at')
    return render(request, 'jobs/home.html', {'jobs': jobs})

def register_job_seeker(request):
    if request.method == 'POST':
        form = JobSeekerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            JobSeeker.objects.create(
                user=user,
                phone=form.cleaned_data['phone'],
                resume=form.cleaned_data['resume'],
                skills=form.cleaned_data['skills'],
                experience=form.cleaned_data['experience']
            )
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = JobSeekerRegistrationForm()
    return render(request, 'registration/register_job_seeker.html', {'form': form})

def register_recruiter(request):
    if request.method == 'POST':
        form = RecruiterRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Recruiter.objects.create(
                user=user,
                company_name=form.cleaned_data['company_name'],
                company_description=form.cleaned_data['company_description']
            )
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = RecruiterRegistrationForm()
    return render(request, 'registration/register_recruiter.html', {'form': form})

@login_required
def post_job(request):
    if not hasattr(request.user, 'recruiter'):
        messages.error(request, 'Only recruiters can post jobs!')
        return redirect('home')
    
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = request.user.recruiter
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobForm()
    return render(request, 'jobs/post_job.html', {'form': form})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    already_applied = False
    if request.user.is_authenticated and hasattr(request.user, 'jobseeker'):
        already_applied = JobApplication.objects.filter(
            job=job,
            applicant=request.user.jobseeker
        ).exists()
    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'already_applied': already_applied
    })

@login_required
def apply_job(request, pk):
    if not hasattr(request.user, 'jobseeker'):
        messages.error(request, 'Only job seekers can apply for jobs!')
        return redirect('job_detail', pk=pk)
    
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user.jobseeker
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('job_detail', pk=pk)
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})

@login_required
def manage_applications(request):
    if not hasattr(request.user, 'recruiter'):
        messages.error(request, 'Only recruiters can manage applications!')
        return redirect('home')
    
    applications = JobApplication.objects.filter(
        job__company=request.user.recruiter
    ).select_related(
        'applicant__user',
        'job'
    ).order_by('-applied_at')
    return render(request, 'jobs/manage_applications.html', {'applications': applications})

@login_required
def update_application_status(request, pk, status):
    if not hasattr(request.user, 'recruiter'):
        messages.error(request, 'Only recruiters can update application status!')
        return redirect('home')
    
    application = get_object_or_404(JobApplication, pk=pk)
    if application.job.company != request.user.recruiter:
        messages.error(request, 'You can only update your own job applications!')
        return redirect('manage_applications')
    
    application.status = status
    application.save()

    # If the applicant is hired, update the job status and reject other applications
    if status == 'hired':
        job = application.job
        job.status = 'filled'
        job.hired_applicant = application.applicant
        job.save()
        
        # Reject other pending applications for this job
        JobApplication.objects.filter(
            job=job,
            status='pending'
        ).exclude(
            pk=application.pk
        ).update(status='rejected')
        
        messages.success(request, f'Application accepted and position filled! Other applications have been updated.')
    else:
        messages.success(request, f'Application {status} successfully!')
    
    return redirect('manage_applications')

@login_required
def close_position(request, pk):
    if not hasattr(request.user, 'recruiter'):
        messages.error(request, 'Only recruiters can close positions!')
        return redirect('home')
    
    job = get_object_or_404(Job, pk=pk)
    if job.company != request.user.recruiter:
        messages.error(request, 'You can only close your own job positions!')
        return redirect('home')
    
    job.status = 'closed'
    job.save()
    
    # Reject all pending applications
    JobApplication.objects.filter(
        job=job,
        status='pending'
    ).update(status='rejected')
    
    messages.success(request, 'Position closed successfully! All pending applications have been rejected.')
    return redirect('job_detail', pk=pk)
