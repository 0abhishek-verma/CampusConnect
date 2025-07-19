from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import*
from .serializers import*
# Create your views here.

class AssignmentListView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        assignment = Assignment.objects.all()
        serializer_data = AssignmentSerializer(assignment, many =True)
        return Response(serializer_data.data,status=status.HTTP_200_OK)
    
class AssignmentSubmissionListView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        if request.user.role == 'student' or request.user.role == 'teacher' :
            assignment = AssignmentSubmission.objects.all()
            serializer_data = AssignmentSubmissionSerializer(assignment, many =True)
            return Response(serializer_data.data,status=status.HTTP_200_OK)
        return Response({'message':'You dont have permission'},status=status.HTTP_401_UNAUTHORIZED)
    
    def post(self,request):
        user = request.user
        student = request.data.get('student')
        if user.role == 'student':
            if AssignmentSubmission.objects.filter(student=student).exists():
                submitting = AssignmentSubmission.objects.get(student=student)
                if submitting.submitted_on:
                    return Response({"message": "Already submitted"}, status=status.HTTP_200_OK)
            serializer_data = AssignmentSubmissionSerializer(data=request.data)
            if serializer_data.is_valid():
                serializer_data.save()
                return Response(serializer_data.data, status=status.HTTP_201_CREATED)
            return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'You dont have permission'},status=status.HTTP_401_UNAUTHORIZED)