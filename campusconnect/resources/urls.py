from django.urls import path
from .views import *
urlpatterns = [
    path('resources-view/',ResourcesView.as_view(),name="ResourcesView")
]
