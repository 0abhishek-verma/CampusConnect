from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'
        
class SemesterSerializer(serializers.ModelSerializer):
    subject = serializers.ReadOnlyField(source='Subjects.name')
    code = serializers.ReadOnlyField(source='Subjects.code')
    class Meta:
        model = Semester
        fields = '__all__'