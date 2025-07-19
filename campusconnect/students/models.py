from django.db import models
from accounts.models import CustomUser
from core.models import Department
# Create your models here.
class StudentProfile(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    enrollment_number = models.CharField(max_length=20,unique=True)
    batch = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)