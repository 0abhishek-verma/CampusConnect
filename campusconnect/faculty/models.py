from django.db import models
from accounts.models import CustomUser
from core.models import Department

# Create your models here.
class FacultyProfile(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=100,unique=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    