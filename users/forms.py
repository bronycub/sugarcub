from django             import forms
from registration.forms import RegistrationFormUniqueEmail
from multiform          import MultiModelForm, InvalidArgument
from .models            import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model   = Profile
        exclude = ['user', 'addressLatitude', 'addressLongitude']

class RegistrationForm(MultiModelForm):

    base_forms = [
        ('registration', RegistrationFormUniqueEmail),
        ('profile',      ProfileForm),
    ]

    def dispatch_init_instance(self, name, instance):
        if name == 'registration':
            return InvalidArgument
        return super(RegistrationForm, self).dispatch_init_instance(name, instance)

    def save(self, commit=True, user=None):
        """Save both forms and attach the user to the profile."""
        instances = self._combine('save', call=True, ignore_missing=True, call_kwargs={'commit': False})
        instances['profile'].user = user
        instances['profile'].save()
        return instances

