from django.db import models
from accounts.models import CustomUser
# Create your models here.
class Notifications(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)