from django.db import models
from restaurants.models import Restaurant
# Create your models here.
class MenuCategory(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    display_order = models.IntegerField()

    def __str__(self):
        return f"{self.restaurant.name} - {self.name}"
    
class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_veg = models.BooleanField(default=True)
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name