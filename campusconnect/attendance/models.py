from django.db import models
from students.models import StudentProfile
from core.models import Subjects
# Create your models here.

class Attendance(models.Model):
    student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    Subjects = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50, choices= [('present','Present'),('absent','Absent')])