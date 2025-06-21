from rest_framework import serializers
from .models import Restaurant
from menu.models import MenuCategory, MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class MenuCategorySerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'display_order', 'items']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class RestaurantDetailSerializer(serializers.ModelSerializer):
    categories = MenuCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'
