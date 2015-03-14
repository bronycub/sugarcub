from django             import forms
from registration.forms import RegistrationFormUniqueEmail
from multiform          import MultiForm
from .models            import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model   = Profile
        exclude = ['user', 'addressLatitude', 'addressLongitude']

class SignupForm(MultiForm):

    base_forms = [
        ('user',	RegistrationFormUniqueEmail),
        ('profile', ProfileForm),
    ]

