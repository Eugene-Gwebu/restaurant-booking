from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default='Name', max_length=200)
    last_name = models.CharField(default='Surname', max_length=200)
    email = models.EmailField(default='example@example.com', max_length=200)
    phone_number = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"