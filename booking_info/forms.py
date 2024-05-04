from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)
        


    def save(self, commit=True):
        """
        Save method to edit profile information.
        """
        profile = super(ProfileForm, self).save(commit=False)
        
        user = profile.user
        # get the current user
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']
        profile.email = self.cleaned_data['email']
        profile.phone_number = self.cleaned_data['phone_number'] 
        
        if commit:
            user.save()
            profile.save()
        return profile