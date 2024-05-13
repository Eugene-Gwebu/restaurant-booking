"""
URL configuration for the_lunchbar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from booking_system.views import my_booking
# from contact.views import contact_us
urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("menu/", include("menu.urls"), name="menu-urls"),
    path('admin/', admin.site.urls),
    path('contact/', include("contact.urls"), name="contact-urls"),
    path('', include("booking_system.urls")), 
    # path('contact/', contact_us, name='contact'), 
]
