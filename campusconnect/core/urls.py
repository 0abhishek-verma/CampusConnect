from django.urls import path
from .views import *
urlpatterns = [
    path('department/',DepartmentView.as_view(),name='department'),
    path('semester/',Semesterview.as_view(),name='semester'),
    path('subjects/',SubjectView.as_view(),name='subjects'),
    
]
