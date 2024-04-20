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

    def save(self, commit=True):
        """
        Save method to edit booking information.
        """
        edit_booking = super(ConfirmBookingForm, self).save(commit=False)
        
        booking = edit_booking
        booking.first_name = self.cleaned_data['first_name']
        booking.last_name = self.cleaned_data['last_name']
        booking.email = self.cleaned_data['email']
        booking.date = self.cleaned_data['date'] 
        booking.time = self.cleaned_data['time']
        if commit:
            booking.save()
            edit_booking.save()
        return edit_booking
       