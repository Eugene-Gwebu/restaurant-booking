from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('your_name', 'your_email', 'subject', 'additional_comments')

     