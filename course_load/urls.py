from django.urls import path
from django.shortcuts import redirect
from django.views.generic import TemplateView
from course_load.views import (hod_views, shared_views, admin_views)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('dashboard/', login_required(TemplateView.as_view(template_name='index.html'))),
    path('', lambda request: redirect('/course-load/dashboard', permanent=False)),
    path('dashboard/', hod_views.DashboardView.as_view()),
    path('get-data/', hod_views.get_data),
    path('get-course-data/', hod_views.get_course_data),
    path('clear-course/', hod_views.clear_course),
    path('submit-data/', hod_views.submit_data),
    path('add-comment/', hod_views.AddComment.as_view()),
    path('request-course-access/', hod_views.request_course_access),
    path('download-course-wise/', shared_views.download_course_wise),
    path('download-instructor-wise/', shared_views.download_instructor_wise),
    path('download-erp/', admin_views.download_erp),
    path('download-time-table/', admin_views.download_time_table),
    path('download-format-5/', admin_views.download_instructor_wise_compressed),
    path('download-data-template/', admin_views.download_data_template),
    path('download-past-course-strength-data-template/', admin_views.download_past_course_strength_data_template),
    path('download-course-data-template/', admin_views.download_course_data_template),
    path('download-instructor-data-template/', admin_views.download_instructor_data_template),
    path('download-database-dump/', admin_views.download_database_dump),
    path('toggle-portal/', admin_views.TogglePortal.as_view()),
    path('upload-initial-data/', admin_views.UploadInitialData.as_view()),
    path('upload-past-course-strength-data/', admin_views.UploadPastCourseStrengthData.as_view()),
    path('get-course-history/', admin_views.get_course_history),
    path('course-history/', admin_views.ViewCourseHistory.as_view()),
]