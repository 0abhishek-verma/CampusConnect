from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import*
from .serializers import*
# Create your views here.

class AssignmentListView(APIView):
    def get(self,request):
        assignment = Assignment.objects.all()
        serializer_data = AssignmentSerializer(assignment, many =True)
        return Response(serializer_data.data,status=status.HTTP_200_OK)
    
class AssignmentSubmissionListView(APIView):
    def get(self,request):
        assignment = AssignmentSubmission.objects.all()
        serializer_data = AssignmentSubmissionSerializer(assignment, many =True)
        return Response(serializer_data.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer_data = AssignmentSubmissionSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)