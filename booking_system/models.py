from django.db import models
from django.contrib.auth.models import User
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Booking(models.Model):
    full_name = models.CharField(default='Name Surname', max_length=200, unique=True)
    email = models.EmailField(default='example@example.com', max_length=200, unique=True)
    phone_number = models.CharField(max_length=40, blank=True, null=True)
    places = models.PositiveIntegerField(
        default=1, 
        validators=[
            MaxValueValidator(10), 
            MinValueValidator(1)])
    date = models.DateField() 
    time = models.TimeField()
    cancel = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"You have received a booking from {self.full_name} ({self.email}) | on {self.date} | at {self.time}."



