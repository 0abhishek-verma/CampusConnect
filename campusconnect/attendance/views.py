from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response

from datetime import date

from .models import *
from students.models import *

from .serializers import *

# Create your views here.

class StudentAttendanceView(APIView):
    def post(self,request):
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
    
    def get(self,request):
        attendance = Attendance.objects.all()
        serializer_data = AttendanceSerializer(attendance,many=True)
        return Response(serializer_data.data,status=status.HTTP_200_OK)  


class ViewAttendance(APIView):
    def get(self,request):
        id= request.data.get('student')
        if Attendance.objects.filter(student=id).exists():
            attendance = Attendance.objects.filter(student=id)
            serializer_data = AttendanceSerializer(attendance,many=True)
            return Response(serializer_data.data,status=status.HTTP_200_OK)  
        return Response
