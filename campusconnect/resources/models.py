from django.db import models
from faculty.models import FacultyProfile
from core.models import Subjects
# Create your models here.

class Resources(models.Model):
    title=models.CharField(max_length=50)
    file = models.FileField(upload_to = 'Resources/')
    uploaded_by =models.ForeignKey(FacultyProfile,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    uploaded_on =models.DateField(auto_now_add=True)