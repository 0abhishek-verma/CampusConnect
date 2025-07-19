from django.urls import path
from .views import *
urlpatterns = [
    path('show-assignment/',AssignmentListView.as_view(),name='show-assignment/'),
    path('submitted-assignment/',AssignmentSubmissionListView.as_view(),name='submitted-assignment/')
    
]
