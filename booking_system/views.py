from django.shortcuts import render, get_object_or_404, reverse
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
#      template_name = "booking_system/home.html"
#      template_name = "booking_system/index.html"

def home(request):

     return render(request, 'booking_system/home.html')


@login_required
def booking_form(request):

     booking = Booking.objects.all()

     confirm_booking_form = ConfirmBookingForm()
     if request.method == "POST":
          confirm_booking_form = ConfirmBookingForm(data=request.POST)
          if confirm_booking_form.is_valid():
               booking = confirm_booking_form.save()
               
               messages.add_message(
                    request, messages.SUCCESS,
                    'Your booking was submitted successfully, and will be approved shortly!'
               )

     
     return render(
          request,
          "booking_system/booking_form.html",
          {
               "booking": booking,
               "confirm_booking_form": confirm_booking_form,
          },
     )

@login_required
def edit_booking(request, booking_id):
    """
    View to edit a booking
    """
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == "POST":
        confirm_booking_form = ConfirmBookingForm(data=request.POST, instance=booking)
        if confirm_booking_form.is_valid():
            confirm_booking_form.save()
            messages.success(request, 'Your Booking Has Been Updated!')
            return redirect('booking_detail', booking_id=booking_id)
        else:
            messages.error(request, 'Error updating booking!')

    else:
        confirm_booking_form = ConfirmBookingForm(instance=booking)
    
    return render(request, 'booking_system/booking_info.html', {'confirm_booking_form': confirm_booking_form})










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