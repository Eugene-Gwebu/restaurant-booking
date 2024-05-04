from . import views
from django.urls import path 

urlpatterns = [
    # path('', views.ContactList.as_view(), name='contact_us'),
    path('', views.contact_form, name='contact_form'),
]