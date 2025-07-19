from rest_framework import serializers
from .models import CustomUser

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email','password','role','is_staff','first_name','last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }
