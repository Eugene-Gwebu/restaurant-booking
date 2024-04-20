from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='homepage'),
    path('booking/', views.booking_form, name='booking_form'),
    path('booking/booking_form/<int:booking_id>/', views.edit_booking, name='edit_booking'),
]