from .models import Booking
from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime



class ConfirmBookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'places', 'date', 'time')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(
            attrs={'type': 'date', 'min': datetime.now().strftime("%Y-%m-%d")})
        self.fields['time'].widget = forms.widgets.TimeInput(
            attrs={'type': 'time'})

    def clean(self):
        """
        Claen method to prevent double-booking.
        """

        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        email = cleaned_data.get('email')

        if date and time and email:
            if Booking.objects.filter(date=date, time=time, email=email).exists():
                raise ValidationError("A booking for this date, time, and email already exists.")

        return cleaned_data


    # def save(self, commit=True):
    #     """
    #     Save method to edit booking information.
    #     """
    #     edit_booking = super(ConfirmBookingForm, self).save(commit=False)
        
    #     booking = edit_booking
    #     booking.first_name = self.cleaned_data['first_name']
    #     booking.last_name = self.cleaned_data['last_name']
    #     booking.email = self.cleaned_data['email']
    #     booking.phone_number = self.cleaned_data['phone_number']
    #     booking.places = self.cleaned_data['places'] 
    #     booking.date = self.cleaned_data['date'] 
    #     booking.time = self.cleaned_data['time']

    #     if commit:
    #         booking.save()
    #         edit_booking.save()
    #     return edit_booking
       