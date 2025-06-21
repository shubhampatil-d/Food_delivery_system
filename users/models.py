from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model



# Create your models here.



class Address(models.Model):
    
    user= models.ForeignKey(
        'User', 
        related_name='addresses',
        on_delete=models.CASCADE
        )
    label=models.CharField(max_length=30, choices=[('home','Home'), ('work','Work'), ('other', 'Other')])
    address=models.TextField()
    latitude=models.FloatField()
    longitude=models.FloatField()
    is_default=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.label}- {self.user.username}"

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    default_address= models.ForeignKey(
        'Address',
        null=True, 
        blank=True, 
        on_delete= models.SET_NULL,
        related_name='default_for_users'
        )
    
    def __str__(self):
        return self.username