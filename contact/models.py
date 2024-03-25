from django.db import models

# Create your models here.

class ContactUs(models.Model):
    your_name = model.CharField(max_length=200)
    your_email = model.CharField(max_length=200)
    subject = model.CharField(max_length=200)