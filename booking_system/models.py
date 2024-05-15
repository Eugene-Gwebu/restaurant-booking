from django.db import models
from django.contrib.auth.models import User
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Booking(models.Model):

    # def get_default_profile():
    #     # Get the superuser 'eugene'
    #     superuser = User.objects.get(username='eugene')
    #     # Get or create the associated profile
    #     profile, created = Profile.objects.get_or_create(user=superuser)
    #     return profile
    
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booked_guest")
    first_name = models.CharField(default='Name', max_length=200)
    last_name = models.CharField(default='Surname', max_length=200)
    email = models.EmailField(default='example@example.com', max_length=200)
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
    approval = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]


    def __str__(self):
        return f"You have received a booking from {self.first_name} {self.last_name} ({self.email}) | on {self.date} | at {self.time}."




