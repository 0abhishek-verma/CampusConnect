
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication

from .serializers import *
from .models import * 
# Create your views here.

class UserRegisterView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self,request):
        data = request.data.copy()
        if data.get('role','').lower() == 'admin':
            data['is_staff'] = True
        
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            return Response(UserRegisterSerializer(user).data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        user = CustomUser.objects.all()
        serializer = UserRegisterSerializer(user,many=True)
        return Response(serializer.data)
    
    def patch(self,request):
        id= request.data.get('id')
        print('fdianvieafvid',id)
        user = CustomUser.objects.filter(id=id).first()
        if user:
            user = CustomUser.objects.get(id=id)
            
            serializer = UserRegisterSerializer(user, data=request.data, partial= True)
            if serializer.is_valid():
                user = serializer.save()
                user.set_password(request.data.get('password'))
                user.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'message':'ID does not exists'}, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self,request):
        id = request.data.get('id')
        print(id,'cdijbcifiudigadccdugasdsdsade')
        custom_data = CustomUser.objects.filter(id=id).exists()
        print(custom_data,'uhfsipyergsofyedsfuds7weudv')
        if custom_data:
            CustomUser.objects.get(id=id).delete()
            return Response({'message':'Deleted Successfully'},status=status.HTTP_200_OK)
        return Response({'message':'ID not found'},status=status.HTTP_200_OK)
    
    
class LoginView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password =request.data.get('password')
        
        user = authenticate(username=username,password=password)
        print(user)
        if user:
            token,_ =Token.objects.get_or_create(user=user)
            return Response(
                {
                    'user': UserRegisterSerializer(user).data,
                    'token':token.key
                },
                status= status.HTTP_201_CREATED
            )
        return Response({
            'error':'Invalid Credientials'
        },status=status.HTTP_400_BAD_REQUEST)
        
class LogoutView(APIView):
    permission_classes =[IsAuthenticated]
    authentication_classes =[TokenAuthentication]
    def post(self,request):
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)

        
    