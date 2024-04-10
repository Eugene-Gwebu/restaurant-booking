from django.shortcuts import render
from django.views import generic 
from .models import Booking

# Create your views here.

# class BookingList(generic.ListView):
#      queryset = Booking.objects.all()
#      template_name = "booking_system/home.html"
#      template_name = "booking_system/index.html"

def home(request):

     return render(request, 'booking_system/home.html')


def booking_form(request):

     return render(request, 'booking_system/booking_form.html')


    