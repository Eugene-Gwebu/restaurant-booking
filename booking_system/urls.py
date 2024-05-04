from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='homepage'),
    path('booking/', views.booking_form, name='booking'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('cancel_booking/<int:booking_id>', views.cancel_booking, name='cancel_booking'),
    path('confirmed_booking/', views.confirmed_booking, name='confirmed_booking'),
]