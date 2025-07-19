from django.urls import path
from .views import *
urlpatterns = [
    path('dashboard/',StudentUpdateView.as_view(),name='student-dashboard')
]
