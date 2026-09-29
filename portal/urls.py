from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('departments/', views.departments, name='departments'),
    path('faculty/', views.faculty_list, name='faculty'),
    path('notices/', views.notices_list, name='notices'),
    path('notices/<int:notice_id>/download/', views.download_notice_pdf, name='download_notice_pdf'),
    path('gallery/', views.gallery_list, name='gallery'),
    path('facilities/', views.facilities, name='facilities'),
    path('contact/', views.contact, name='contact'),
    path('student/register/', views.student_register, name='student_register'),
    path('student/login/', views.student_login_view, name='student_login'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/login/', views.teacher_login_view, name='teacher_login'),
    path('teacher/attendance/', views.take_attendance, name='take_attendance'),
    path('logout/', views.logout_view, name='logout'),
]
