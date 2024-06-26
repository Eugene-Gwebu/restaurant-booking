from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

# Create your views here.

# class ContactList(generic.ListView):
#     queryset = Contact.objects.all()
#     template_name = "contact/contact.html"
    
def contact_form(request):

     contact = Contact.objects.all()

     if request.method == "POST":
          contact_form = ContactForm(data=request.POST)
          if contact_form.is_valid():
               contact = contact_form.save()
               messages.add_message(
                    request, messages.SUCCESS,
                    'We have received your request, and will be in touch shortly!'
               )

     contact_form = ContactForm()
     
     return render(
          request,
          "contact/contact.html",
          {
               "contact": contact,
               "contact_form": contact_form,
          },
     )