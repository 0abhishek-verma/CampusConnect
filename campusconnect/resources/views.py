from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import *
from faculty.models import *
from core.models import *

from .serializers import *

from django.db.models import Q

# Create your views here.

class ResourcesView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self,request):
        subject_query = request.query_params.get('subject')
        teacher_query = request.query_params.get('teacher')
        resources = Resources.objects.all()
        if subject_query:
            resources =Resources.objects.filter(subject__name__icontains = subject_query)
        if teacher_query:
            resources =Resources.objects.filter(uploaded_by__user__first_name__icontains = teacher_query)
            resources =Resources.objects.filter(uploaded_by__user__last_name__icontains = teacher_query)
        serializer_data = ResourcesSerializer(resources,many=True)
        return Response(serializer_data.data,status=status.HTTP_200_OK)
    def post(self,request):
        user = request.user
        if request.user.role != 'teacher':
            return Response({'message':'You are not allowed to perform this action'},status=status.HTTP_401_UNAUTHORIZED)
        faculty=FacultyProfile.objects.get(user=user)
        subject_id =request.data.get('subject')
        subjects = Subjects.objects.get(id=subject_id)
        if faculty.department != subjects.department:
            return Response({'message':'You are not allowed to perform this action this is not your department'},status=status.HTTP_401_UNAUTHORIZED)
        serializer_data = ResourcesSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data,status=status.HTTP_200_OK)
        return Response(serializer_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        id = request.data.get(id)
        
        