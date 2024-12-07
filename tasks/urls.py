from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('', views.home, name='home'),
    path('register/job-seeker/', views.register_job_seeker, name='register_job_seeker'),
    path('register/recruiter/', views.register_recruiter, name='register_recruiter'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('job/post/', views.post_job, name='post_job'),
    path('job/<int:pk>/apply/', views.apply_job, name='apply_job'),
    path('job/<int:pk>/delete/', views.delete_job, name='delete_job'),
    path('applications/', views.manage_applications, name='manage_applications'),
    path('profile/', views.profile, name='profile'),
    path('resume/update/', views.update_resume, name='update_resume'),
    path('application/<int:application_id>/<str:status>/', views.update_application_status, name='update_application_status'),
]
