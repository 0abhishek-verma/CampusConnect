from rest_framework import serializers
from .models import *


class ResourcesSerializer(serializers.ModelSerializer):
    faculty_name = serializers.ReadOnlyField(source ='uploaded_by.user.get_full_name')
    Subject_name = serializers.ReadOnlyField(source ='subject.name')
    class Meta:
        model=Resources
        fields = '__all__'
