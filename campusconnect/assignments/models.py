from django.db import models
from students.models import StudentProfile
from faculty.models import FacultyProfile
from core.models import Subjects
# Create your models here.

class Assignment(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    file = models.FileField(upload_to='assignment/')
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    Teacher = models.ForeignKey(FacultyProfile, on_delete=models.CASCADE)
    deadline = models.DateField()
    
class AssignmentSubmission(models.Model):
    assignment =models.ForeignKey(Assignment,on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')
    submitted_on =  models.DateTimeField(auto_now_add=True)
    marks = models.PositiveIntegerField(null=True,blank=True,default=0)