from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly


from .models import StudentProfile
from .serializers import StudentProfileSerializer

class StudentUpdateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes =[TokenAuthentication]
    def get(self, request):
        if request.user.role == 'student':
            profiles = StudentProfile.objects.all()
            serializer = StudentProfileSerializer(profiles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'unauthorized access Not allow to view'},status=status.HTTP_401_UNAUTHORIZED)

    

