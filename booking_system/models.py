from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    places = models.IntegerField(min_value=1, max_value=10)
    date = models.DateField() 
    time = models.TimeField()
    cancel_booking = models.ForeignKey(
        Guest, on_delete=models.CASCADE, related_name="booking"
    )


class Guest(models.Model):
    full_name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.IntegerField()


