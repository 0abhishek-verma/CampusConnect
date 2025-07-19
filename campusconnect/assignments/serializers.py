from rest_framework.serializers import ModelSerializer
from .models import *

class AssignmentSerializer(ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'
        
class AssignmentSubmissionSerializer(ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = '__all__'