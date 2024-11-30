from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from tasks import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/job-seeker/', views.register_job_seeker, name='register_job_seeker'),
    path('register/recruiter/', views.register_recruiter, name='register_recruiter'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('post-job/', views.post_job, name='post_job'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('job/<int:pk>/apply/', views.apply_job, name='apply_job'),
    path('job/<int:pk>/close/', views.close_position, name='close_position'),
    path('manage-applications/', views.manage_applications, name='manage_applications'),
    path('application/<int:pk>/<str:status>/', views.update_application_status, name='update_application_status'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
