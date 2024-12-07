from .models import JobSeeker, Recruiter

def user_roles(request):
    context = {
        'is_jobseeker': False,
        'is_recruiter': False,
        'jobseeker': None,
        'recruiter': None
    }
    
    if request.user.is_authenticated:
        # Check for JobSeeker
        jobseeker = JobSeeker.objects.filter(user=request.user).first()
        if jobseeker:
            context['is_jobseeker'] = True
            context['jobseeker'] = jobseeker
            request.is_jobseeker = True
            request.jobseeker = jobseeker
        else:
            request.is_jobseeker = False
            request.jobseeker = None
            
        # Check for Recruiter
        recruiter = Recruiter.objects.filter(user=request.user).first()
        if recruiter:
            context['is_recruiter'] = True
            context['recruiter'] = recruiter
            request.is_recruiter = True
            request.recruiter = recruiter
        else:
            request.is_recruiter = False
            request.recruiter = None
            
    return context
