from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser

from .models import *
from .serializers import *
# Create your views here.


class DepartmentView(APIView):
    def get(self,request):
        if request.user.role != 'admin':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        department = Department.objects.all()
        serializer_data = DepartmentSerializer(department,many=True)
        return Response(serializer_data.data,status=status.HTTP_200_OK) 
    
    def post(self, request):
        if request.user.role != 'admin':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        serializer_data = DepartmentSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data,status=status.HTTP_200_OK)
        return Response(serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        if request.user.role != 'admin':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        id=request.data.get('id')
        department = Department.objects.filter(id=id).exists()
        if department:
            serializer_data = DepartmentSerializer(department,data=request.data,partial=True)
            if serializer_data.is_valid():
                serializer_data=serializer_data.save()
                return Response(DepartmentSerializer(serializer_data).data,status=status.HTTP_200_OK)
            return Response(serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'department not found'},status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request):
        if request.user.role != 'admin':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        id = request.data.get('id')
        department_data = Department.objects.filter(id=id).exists()
        if department_data:
            Department.objects.get(id=id).delete()
            return Response({'message':'Deleted Successfully'},status=status.HTTP_200_OK)
        return Response({'message':'ID not found'},status=status.HTTP_200_OK)
    
    
class Semesterview(APIView):
    
    def post(self,request):
        if request.user.role != 'admin':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        serializer_data = SemesterSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data,status=status.HTTP_200_OK)
        return Response(serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        if request.user.role != 'admin':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        semester_data = Semester.objects.all()
        serializer_data = SemesterSerializer(semester_data,many=True)
        return Response(serializer_data.data)
    
    def patch(self,request):
        if request.user.role != 'admin':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        id=request.data.get('id')
        semester = Semester.objects.filter(id=id).exists()
        if semester:
            serializer_data = SemesterSerializer(semester,data=request.data,partial=True)
            if serializer_data.is_valid():
                serializer_data=serializer_data.save()
                return Response(SemesterSerializer(serializer_data).data,status=status.HTTP_200_OK)
            return Response(serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'semester not found'},status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request):
        if request.user.role != 'admin':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        id = request.data.get('id')
        semester_data = Semester.objects.filter(id=id).exists()
        if semester_data:
            Semester.objects.get(id=id).delete()
            return Response({'message':'Deleted Successfully'},status=status.HTTP_200_OK)
        return Response({'message':'ID not found'},status=status.HTTP_200_OK)
    
class SubjectView(APIView):
    authentication_classes =[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        subject_data = Subjects.objects.all()
        serializer_data = SubjectSerializer(subject_data,many=True)
        return Response(serializer_data.data)
    def post(self,request):
        if request.user.role != 'admin':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        serializer_data = SubjectSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data,status=status.HTTP_200_OK)
        return Response(serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request):
        if request.user.role != 'admin':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        subject_id = request.data.get('id')
        subject_data = Subjects.objects.filter(id=subject_id).exists()
        if subject_data:
            serializer_data = SubjectSerializer(subject_data,data=request.data, partial= True)
            if serializer_data.is_valid():
                serializer_data.save()
                return Response(serializer_data.data,status=status.HTTP_200_OK)
            return Response(serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'subject not found'},status=status.HTTP_404_NOT_FOUND)
    def delete(self,request):
        if request.user.role != 'admin':
            return Response({'message':'You dont have permission'},status=status.HTTP_400_BAD_REQUEST)
        subject_id = request.data.get('id')
        subject_data = Subjects.objects.filter(id=subject_id).exists()
        if subject_data:
            Subjects.objects.get(id=subject_id).delete()
            return Response({'message':'Deleted Successfully'},status=status.HTTP_200_OK)
        return Response({'message':'ID not found'},status=status.HTTP_200_OK)
        

    