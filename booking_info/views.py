from django.shortcuts import render, get_object_or_404, reverse

from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from booking_system .models import Booking


# Create your views here.

@login_required
def profile_form(request, profile_id):

    queryset = Profile.objects.filter(approval=True)
    profile = get_object_or_404(Profile, id=profile_id)

    profile_form = ProfileForm(instance=profile)
    if request.method == "POST":
        profile_form = ProfileForm(data=request.POST, instance=profile)
        if profile_form.is_valid() and profile.user == request.user:
            profile_form.save()
            
    
    return render(
        request,
        "booking_info/profile.html",
        {
            "profile": profile,
            "profile_form": profile_form,
        },
    )

