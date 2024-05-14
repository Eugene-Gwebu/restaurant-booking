from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic 
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Booking
from django.core.mail import send_mail
from .forms import ConfirmBookingForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView 




# Create your views here.


def home(request):

     return render(request, 'booking_system/home.html')


@login_required
def booking_form(request):

    if request.method == "POST":
        confirm_booking_form = ConfirmBookingForm(data=request.POST)
        if confirm_booking_form.is_valid():
            booking = confirm_booking_form.save(commit=False)
            booking.guest =request.user
            booking.save()

            messages.success(request, 'Your booking was submitted successfully, and will be approved shortly!')  
    
    confirm_booking_form = ConfirmBookingForm()

    return render(
        request,
        "booking_system/booking_form.html",
        {
            "confirm_booking_form": confirm_booking_form,
        },
    )
     

@login_required
def confirmed_booking(request):
    """
    View to display booking details
    """
    bookings = Booking.objects.filter(approval=True, guest = request.user)
    guest = request.user

    return render(request, 'booking_system/reservation.html', 
    {
        'guest': guest,
        'bookings': bookings,
    })


@login_required
def edit_booking(request, booking_id):
    """
    View to edit a booking
    """
    booking = get_object_or_404(Booking, pk=booking_id)
    form = ConfirmBookingForm(data=request.POST, instance = booking)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("confirmed_booking"))

    context = {
        "form": form
    }
    
    return render(request, "booking_system/edit_booking.html", context)


@login_required
def cancel_booking(request, booking_id):
    """
    view to cancel a booking
    """
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == "POST":
        
        booking.guest == request.user
        booking.delete()
        messages.add_message(request, messages.SUCCESS, 'Your Booking was successfully deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'Apologies, you cannot cancel this booking at the moment!')
    
    return HttpResponseRedirect(reverse('homepage'))

