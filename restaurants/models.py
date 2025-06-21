from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    cuisine_type = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    operating_hours = models.CharField(max_length=100)
    min_order_amount = models.DecimalField(max_digits=6, decimal_places=2)
    delivery_fee = models.DecimalField(max_digits=5, decimal_places=2)
    avg_prep_time = models.IntegerField(help_text="In minutes")
    status = models.CharField(max_length=10, choices=[('open', 'Open'), ('closed', 'Closed')])
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
