from rest_framework import serializers
from . models import *


class FacultyProfileSerializer(serializers.ModelSerializer):
    first_name =serializers.ReadOnlyField(source='user.first_name')
    last_name =serializers.ReadOnlyField(source='user.last_name')
    email =serializers.ReadOnlyField(source='user.email')
    department_name =serializers.ReadOnlyField(source='department.name')
    class Meta:
        model=FacultyProfile
        fields = '__all__'