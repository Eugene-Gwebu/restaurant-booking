from . import views
from django.urls import path 

urlpatterns = [
    path('', views.ContactList.as_view(), name='contact_us'),
    path('menu/', views.menu, name='menu'),
]