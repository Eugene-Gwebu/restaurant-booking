from .models import Booking
from django import forms
from datetime import datetime



class ConfirmBookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'places', 'date', 'time')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(
            attrs={'type': 'date'})
        self.fields['time'].widget = forms.widgets.TimeInput(
            attrs={'type': 'time'})

       