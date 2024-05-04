from django.urls import path
from . import views 

urlpatterns = [
    # path('', views.profile_form, name='profile'),
    path('profile/<int:profile_id>/', views.profile_form, name='profile_form'),
]