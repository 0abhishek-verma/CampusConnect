from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    
class Semester(models.Model):
    semester = models.IntegerField()
    
class Subjects(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    Semester =models.ForeignKey(Semester,on_delete=models.CASCADE,null=True, blank=True)