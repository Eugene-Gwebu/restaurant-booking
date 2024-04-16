from .models import Booking
from django import forms


class ConfirmBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'places', 'date', 'time')

       