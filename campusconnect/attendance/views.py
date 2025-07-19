from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser

from datetime import date

from .models import *
from students.models import *

from .serializers import *

# Create your views here.

class StudentAttendanceView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
            attendance = Attendance.objects.all()
            serializer_data = AttendanceSerializer(attendance,many=True)
            return Response(serializer_data.data,status=status.HTTP_200_OK)  
        
    def post(self,request):
        print(request.user.role)
        if request.user.role != 'teacher':
            return Response({'message':'You dont have access to perform this action'},status=status.HTTP_401_UNAUTHORIZED)
        data = request.data
        student = data.get('student')
        today = date.today()
        
        if not StudentProfile.objects.filter(id=student).exists:
            return Response({'message':'Student not found'},status=status.HTTP_404_NOT_FOUND)
        if Attendance.objects.filter(student=student,date=today).exists():
            return Response({'message':'attendance marked already'},status=status.HTTP_400_BAD_REQUEST)
        serializer_data =AttendanceSerializer(data=data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data,status=status.HTTP_200_OK)
        return Response(serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    


class ViewAttendance(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request):
        id= request.data.get('student')
        if Attendance.objects.filter(student=id).exists():
            attendance = Attendance.objects.filter(student=id)
            serializer_data = AttendanceSerializer(attendance,many=True)
            return Response(serializer_data.data,status=status.HTTP_200_OK)  
        return Response
