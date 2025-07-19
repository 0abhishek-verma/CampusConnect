from django.urls import path
from .views import *
urlpatterns = [
    path('student-create/',StudentProfileCreation.as_view(),name='student-create'),
    path('faculty-create/',FacultyProfileCreation.as_view(),name='faculty-create'),
    
]
