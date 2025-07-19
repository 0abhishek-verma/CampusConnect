from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


from .models import FacultyProfile
from assignments.models import *

from assignments.serializers import *
from .serializers import FacultyProfileSerializer

class FacultyUpdateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes =[TokenAuthentication]
    def get(self, request):
        if request.user.role == 'teacher':
            profiles = FacultyProfile.objects.all()
            serializer = FacultyProfileSerializer(profiles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'unauthorized access Not allow to view'},status=status.HTTP_401_UNAUTHORIZED)
    

class AssignmentView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes =[TokenAuthentication]
    def post(self, request):
        if request.user.role != 'teacher':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        serializer_data = AssignmentSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data,status=status.HTTP_200_OK)
        return Response(serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        if request.user.role != 'teacher':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        id = request.data.get('id')
        assignmen_data = Assignment.objects.filter(id=id).exists()
        if assignmen_data:
            
            assignmen_data = Assignment.objects.get(id=id)
            serializer_data = AssignmentSerializer(assignmen_data,data=request.data,partial=True)
            if serializer_data.is_valid():
                serializer_data.save()
            return Response(serializer_data.data,status=status.HTTP_200_OK)
        return Response(serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        if request.user.role != 'teacher':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        id = request.data.get('id')
        assignment_data =Assignment.objects.filter(id=id).exists()
        if assignment_data:
            Assignment.objects.get(id=id).delete()
            return Response({'message':'Deleted Successfully'},status=status.HTTP_200_OK)
        return Response({'message':'ID not found'},status=status.HTTP_200_OK)
    


class AssignmentSubmissionView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes =[TokenAuthentication]
    def patch(self,request):
        if request.user.role != 'teacher':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        id = request.data.get('id')
        assignment_data = AssignmentSubmission.objects.filter(id=id).exists()
        if assignment_data:
            print(assignment_data)
            assignment_data = AssignmentSubmission.objects.get(id=id)
            serializer_data = AssignmentSubmissionSerializer(assignment_data,data=request.data,partial=True)
            print(serializer_data,'ieugdsysd')
            if serializer_data.is_valid():
                print(serializer_data,'ieugdsysd')
                serializer_data.save()
                return Response(serializer_data.data,status=status.HTTP_200_OK)
            return Response(serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'no data found'},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        if request.user.role != 'teacher':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        id = request.data.get('id')
        assignment_data =AssignmentSubmission.objects.filter(id=id).exists()
        if assignment_data:
            AssignmentSubmission.objects.get(id=id).delete()
            return Response({'message':'Deleted Successfully'},status=status.HTTP_200_OK)
        return Response({'message':'ID not found'},status=status.HTTP_200_OK)