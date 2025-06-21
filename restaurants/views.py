from django.shortcuts import render
from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer,RestaurantDetailSerializer

# Create your views here.
class RestaurantListView(generics.ListAPIView):
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        # Optionally filter by proximity later using lat/lng
        return Restaurant.objects.filter(status='open')

class RestaurantDetailView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    lookup_field = 'pk'
