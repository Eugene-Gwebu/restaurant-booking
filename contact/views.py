from django.shortcuts import render
from django.views import generic
from .models import Contact
from .forms import ContactForm

# Create your views here.

# class ContactList(generic.ListView):
#     queryset = Contact.objects.all()
#     template_name = "contact/contact.html"
    
def contact_form(request):

     contact = Contact.objects.all()

     contact_form = ContactForm()
     
     return render(
          request,
          "contact/contact.html",
          {
               "contact": contact,
               "contact_form": contact_form,
          },
     )