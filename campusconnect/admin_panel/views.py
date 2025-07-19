from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser


from students.serializers import StudentProfileSerializer
from faculty.serializers import FacultyProfileSerializer

from students.models import StudentProfile
from faculty.models import FacultyProfile
# Create your views here.
class StudentProfileCreation(APIView):
    # permission_classes = [IsAdminUser]
    # authentication_classes =[TokenAuthentication]
    def get(self, request):
        profiles = StudentProfile.objects.all()
        serializer = StudentProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = StudentProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        id=request.data.get('id')
        student = StudentProfile.objects.filter(id=id).first()
        if student:
            serializer = StudentProfileSerializer(student,data=request.data,partial=True)
            if serializer.is_valid():
                student =serializer.save()
                return Response(
                    StudentProfileSerializer(student).data,status=status.HTTP_200_OK
                )
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'invalid user'},status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self,request):
        id = request.data.get('id')
        student_data = StudentProfile.objects.filter(id=id).exists()
        if student_data:
            StudentProfile.objects.get(id=id).delete()
            return Response({'message':'Deleted Successfully'},status=status.HTTP_200_OK)
        return Response({'message':'ID not found'},status=status.HTTP_200_OK)
    
class FacultyProfileCreation(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes =[TokenAuthentication]
    def post(self, request):
        serializer = FacultyProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        id=request.data.get('id')
        student = FacultyProfile.objects.filter(id=id).first()
        if student:
            serializer = FacultyProfileSerializer(student,data=request.data,partial=True)
            if serializer.is_valid():
                student =serializer.save()
                return Response(
                    FacultyProfileSerializer(student).data,status=status.HTTP_200_OK
                )
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'invalid user'},status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        id = request.data.get('id')
        faculty_data = FacultyProfile.objects.filter(id=id).exists()
        if faculty_data:
            FacultyProfile.objects.get(id=id).delete()
            return Response({'message':'Deleted Successfully'},status=status.HTTP_200_OK)
        return Response({'message':'ID not found'},status=status.HTTP_200_OK)