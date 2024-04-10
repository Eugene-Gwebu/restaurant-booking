from . import views
from django.urls import path 

urlpatterns = [
    path('', views.ContactList.as_view(), name='contact'),
    path('menu/', views.menu, name='menu'),
]