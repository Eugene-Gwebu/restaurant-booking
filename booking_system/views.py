from django.shortcuts import render
from django.views import generic 
from .models import Booking
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.

# class BookingList(generic.ListView):
#      queryset = Booking.objects.all()
#      template_name = "booking_system/home.html"
#      template_name = "booking_system/index.html"

def home(request):

     return render(request, 'booking_system/home.html')


def booking_form(request):

     return render(request, 'booking_system/booking_form.html')


# def booking_confirmation_view(request):
#     if request.method == 'POST':
#         # Extract form data
#         full_name = request.POST.get('full_name')
#         email = request.POST.get('email')
#         phone_number = request.POST.get('phone_number')
#         places = request.POST.get('places')
#         date = request.POST.get('date')
#         time = request.POST.get('time')

#         # Save Booking instance (optional)
#         booking = Booking.objects.create(
#             full_name=full_name,
#             email=email,
#             phone_number=phone_number,
#             places=places,
#             date=date,
#             time=time
#         )

#         # Send confirmation email
#         send_confirmation_email(full_name, email)

#         return HttpResponse("Confirmation email sent successfully!")

#     return HttpResponse("Form not submitted!")

# def send_confirmation_email(full_name, email):
#     subject = 'Booking Confirmation'
#     message = f'Dear {full_name},\n\nThank you for your booking! We have received your information and will get back to you shortly'
#     sender = 'lunchbar@outlook.com'  
#     recipient = [email]
#     send_mail(subject, message, sender, recipient)