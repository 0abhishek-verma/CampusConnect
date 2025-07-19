from django.urls import path
from .views import *
urlpatterns = [
    path('student-attendance/',StudentAttendanceView.as_view(),name='student-attendance'),
    path('student-view-attendance/',ViewAttendance.as_view(),name='student-view-attendance'),
]
