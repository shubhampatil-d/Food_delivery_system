from django.shortcuts import render
from rest_framework import status
from rest_framework.response  import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# Create your views here.

class RegisterView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user= serializer.save()
            return Response({'message': 'user register successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token= super().get_token(user)
        token['username']= user.username
        token['email']= user.email
        return token

class LoginView(TokenObtainPairView):
    serializer_class= CustomTokenObtainPairSerializer