from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.response  import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, AddressSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Address

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


class AddressListCreateView(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SetDefaultAddressView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Address.objects.all()

    def put(self, request, pk):
        user = request.user
        try:
            address = Address.objects.get(pk=pk, user=user)
            Address.objects.filter(user=user).update(is_default=False)
            address.is_default = True
            address.save()
            return Response({'message': 'Default address set'}, status=status.HTTP_200_OK)
        except Address.DoesNotExist:
            return Response({'error': 'Address not found'}, status=status.HTTP_404_NOT_FOUND)
