from django.shortcuts import render
from django.views import generic
from .models import Contact

# Create your views here.

class ContactList(generic.ListView):
    queryset = Contact.objects.all()
    template_name = "contact/contact.html"
    template_name = "contact/menu.html"