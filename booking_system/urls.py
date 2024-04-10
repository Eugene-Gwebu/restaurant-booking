from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='homepage'),
    path('booking/', views.booking_form, name='booking_form'),
]