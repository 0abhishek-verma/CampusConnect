from rest_framework import serializers
from .models import StudentProfile
from accounts.serializers import UserRegisterSerializer
from core.serializers import DepartmentSerializer
class StudentProfileSerializer(serializers.ModelSerializer):
    firstname = serializers.ReadOnlyField(source='user.first_name')
    lastname = serializers.ReadOnlyField(source='user.last_name')
    email = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = StudentProfile
        fields = '__all__'
