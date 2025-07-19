from django.urls import path
from .views import *
urlpatterns = [
    path('faculty-dashboard/',FacultyUpdateView.as_view(),name='faculty-dashboard'),
    path('assignments/',AssignmentView.as_view(),name='assignment'),
    path('assignment-reviewed/',AssignmentSubmissionView.as_view(),name='assignment-reviewed'),
]
