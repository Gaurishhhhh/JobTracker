from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Job, JobSeeker, Recruiter, JobApplication
from .forms import JobSeekerRegistrationForm, RecruiterRegistrationForm, JobApplicationForm, JobPostForm, ResumeUpdateForm

@require_GET
def health_check(request):
    """
    Health check endpoint for Docker/AWS health monitoring
    """
    return JsonResponse({"status": "healthy"}, status=200)

def home(request):
    jobs = Job.objects.filter(status='open').order_by('-created_at')
    return render(request, 'jobs/home.html', {'jobs': jobs})

@login_required
def profile(request):
    jobseeker = JobSeeker.objects.filter(user=request.user).first()
    if not jobseeker:
        messages.error(request, 'Only job seekers can access this page.')
        return redirect('home')
    
    if request.method == 'POST':
        phone = request.POST.get('phone')
        skills = request.POST.get('skills')
        experience = request.POST.get('experience')
        resume = request.FILES.get('resume')
        
        jobseeker.phone = phone
        jobseeker.skills = skills
        jobseeker.experience = experience
        if resume:
            jobseeker.resume = resume
        jobseeker.save()
        
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    
    return render(request, 'jobs/profile.html', {'jobseeker': jobseeker})

@login_required
def update_resume(request):
    jobseeker = JobSeeker.objects.filter(user=request.user).first()
    if not jobseeker:
        messages.error(request, 'Only job seekers can update their resume.')
        return redirect('home')
    
    if request.method == 'POST':
        form = ResumeUpdateForm(request.POST, request.FILES, instance=jobseeker)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resume updated successfully!')
            return redirect('update_resume')
    else:
        form = ResumeUpdateForm(instance=jobseeker)
    
    return render(request, 'jobs/update_resume.html', {
        'form': form,
        'job_seeker': jobseeker
    })

@login_required
def update_application_status(request, application_id, status):
    if request.method == 'POST':
        recruiter = Recruiter.objects.filter(user=request.user).first()
        if not recruiter:
            messages.error(request, 'Only recruiters can update application status.')
            return redirect('home')
        
        application = get_object_or_404(JobApplication, id=application_id)
        if application.job.company != recruiter:
            messages.error(request, 'You can only update status for your own job applications.')
            return redirect('manage_applications')
        
        application.status = status
        application.save()
        
        status_display = 'accepted' if status == 'accepted' else 'rejected'
        messages.success(request, f'Application has been {status_display}.')
        
    return redirect('manage_applications')

@login_required
def delete_job(request, pk):
    if request.method == 'POST':
        recruiter = Recruiter.objects.filter(user=request.user).first()
        if not recruiter:
            messages.error(request, 'Only recruiters can remove jobs.')
            return redirect('home')
        
        job = get_object_or_404(Job, pk=pk)
        if job.company != recruiter:
            messages.error(request, 'You can only remove your own job postings.')
            return redirect('home')
        
        job.delete()
        messages.success(request, 'Job posting has been removed successfully.')
        return redirect('home')
    
    return redirect('job_detail', pk=pk)

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
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')
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
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')
    else:
        form = RecruiterRegistrationForm()
    return render(request, 'registration/register_recruiter.html', {'form': form})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    already_applied = False
    
    if request.user.is_authenticated:
        jobseeker = JobSeeker.objects.filter(user=request.user).first()
        if jobseeker:
            already_applied = JobApplication.objects.filter(
                job=job, applicant=jobseeker
            ).exists()
            
    return render(request, 'jobs/job_detail.html', {
        'job': job,
        'already_applied': already_applied
    })

@login_required
def post_job(request):
    recruiter = Recruiter.objects.filter(user=request.user).first()
    if not recruiter:
        messages.error(request, 'Only recruiters can post jobs.')
        return redirect('home')
    
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = recruiter
            job.save()
            messages.success(request, 'Job posted successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobPostForm()
    
    return render(request, 'jobs/post_job.html', {'form': form})

@login_required
def apply_job(request, pk):
    jobseeker = JobSeeker.objects.filter(user=request.user).first()
    if not jobseeker:
        messages.error(request, 'Only job seekers can apply for jobs.')
        return redirect('home')
    
    job = get_object_or_404(Job, pk=pk)
    
    # Check if already applied
    if JobApplication.objects.filter(job=job, applicant=jobseeker).exists():
        messages.error(request, 'You have already applied for this job.')
        return redirect('job_detail', pk=job.pk)
    
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = jobseeker
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('job_detail', pk=job.pk)
    else:
        form = JobApplicationForm()
    
    return render(request, 'jobs/apply_job.html', {
        'job': job,
        'jobseeker': jobseeker,
        'form': form
    })

@login_required
def manage_applications(request):
    recruiter = Recruiter.objects.filter(user=request.user).first()
    if not recruiter:
        messages.error(request, 'Only recruiters can manage applications.')
        return redirect('home')
    
    jobs = Job.objects.filter(company=recruiter)
    applications = JobApplication.objects.filter(job__in=jobs).order_by('-applied_at')
    return render(request, 'jobs/manage_applications.html', {
        'applications': applications,
        'is_recruiter': True
    })
