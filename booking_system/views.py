from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic 
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Booking
from django.core.mail import send_mail
from .forms import ConfirmBookingForm
from django.contrib.auth.decorators import login_required




# Create your views here.

# class BookingList(generic.ListView):
#      queryset = Booking.objects.all()
#      template_name = "booking_system/reservation.html"
#      template_name = "booking_system/index.html"

def home(request):

     return render(request, 'booking_system/home.html')


@login_required
def booking_form(request):
    if request.method == "POST":
        confirm_booking_form = ConfirmBookingForm(data=request.POST)
        if confirm_booking_form.is_valid():
            booking = confirm_booking_form.save(commit=False)
            profile = request.user
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
    profile = request.user
    bookings = Booking.objects.filter(approval=True)
   
    return render(request, 'booking_system/reservation.html', 
    {
        'bookings':bookings,
    })


@login_required
def edit_booking(request, booking_id):
    """
    View to edit a booking
    """
    if request.method == "POST":

        queryset = Booking.objects.filter(approval=True)
        booking = get_object_or_404(queryset, id=booking_id)
        booking = get_object_or_404(Booking, pk=booking_id)
        confirm_booking_form = ConfirmBookingForm(data=request.POST, instance=booking)
        
        if confirm_booking_form.is_valid() and booking.profile == request.user.profile:
            confirm_booking_form.save(commit=False)
            booking.approval = False
            confirm_booking_form.save()
            messages.success(request, 'Your Booking Has Been Updated!')
            
        else:
            messages.error(request, 'Error updating booking!')
 
    return render(request, 'booking_system/reservation.html', 
    {
        'booking': booking,
        'confirm_booking_form': confirm_booking_form,
    })


@login_required
def cancel_booking(request, booking_id):
    """
    view to cancel a booking
    """
    queryset = Booking.objects.filter(approval=True)
    booking = get_object_or_404(queryset, id=booking_id)

    if booking.profile == request.user:
        booking.delete()
        messages.add_message(request, messages.SUCCESS, 'Your Booking was successfully deleted!')

    else:
        messages.add_message(request, messages.ERROR, 'Apologies, you cannot cancel this booking at the moment!')

    return render(request,'booking_system/reservation.html', 
    {
        'booking': booking,
    })







     # queryset = Booking.objects.filter(approval=True)
     # booking = get_object_or_404(queryset, email=email)
     # if request.method == 'POST':
     #      booking_form = BookingForm(data=request.POST)
     #      if form.is_valid():
         
         
     #      # Extract form data
     #      first_name = request.POST.get('first_name')
     #      last_name = request.POST.get('last_name')
     #      email = request.POST.get('email')
     #      phone_number = request.POST.get('phone_number')
     #      places = request.POST.get('places')
     #      date = request.POST.get('date')
     #      time = request.POST.get('time')

     #      # Save Booking instance (optional)
     #      booking = Booking.objects.create(
     #           full_name=full_name,
     #           email=email,
     #           phone_number=phone_number,
     #           places=places,
     #           date=date,
     #           time=time
     #      )

     #      # Send confirmation email
     #      send_confirmation_email(full_name, email)

     #      return HttpResponse("Confirmation email sent successfully!")

     # return HttpResponse("Form not submitted!")

     # def send_confirmation_email(full_name, email):
     # subject = 'Booking Confirmation'
     # message = f'Dear {full_name},\n\nThank you for your booking! We have received your information and will get back to you shortly'
     # sender = 'lunchbar@outlook.com'  
     # recipient = [email]
     # send_mail(subject, message, sender, recipient)