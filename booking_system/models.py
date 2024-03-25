from django.db import models
from django.contrib.auth.models import User
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Guest(models.Model):
    full_name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.IntegerField()


class Booking(models.Model):
    places = models.IntegerField(
        default=1, 
        validators=[
            MaxValueValidator(10), 
            MinValueValidator(1)])
    date = models.DateField() 
    time = models.TimeField()
    guest = models.ForeignKey(
        Guest, on_delete=models.CASCADE, related_name="booking" #
    )
    cancel = models.BooleanField()



