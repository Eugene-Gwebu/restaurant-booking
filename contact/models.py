from django.db import models

# Create your models here.

class ContactUs(models.Model):
    your_name = models.CharField(max_length=200)
    your_email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)