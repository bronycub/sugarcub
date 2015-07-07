from django                     import forms
from registration.forms         import RegistrationFormUniqueEmail
from multiform                  import MultiModelForm, InvalidArgument
from .models                    import Profile
from django.contrib.auth.models import User
from django.utils.translation   import ugettext_lazy                    as _


class UserForm(forms.ModelForm):

    class Meta:
        model  = User
        fields = ['first_name', 'last_name']


class ProfileForm(forms.ModelForm):

    class Meta:
        model   = Profile
        exclude = ['user', 'addressLatitude', 'addressLongitude']
        labels = {
            "bio": _("Biography"),
            "phone": _("Phone"),
            "birthday": _("Birthday"),
            "address": _("Address"),
        }


class RegistrationForm(MultiModelForm):

    base_forms = [
        ('registration', RegistrationFormUniqueEmail),
        ('user',         UserForm),
        ('profile',      ProfileForm),
    ]

    def dispatch_init_instance(self, name, instance):
        if name == 'registration':
            return InvalidArgument
        return super(RegistrationForm, self).dispatch_init_instance(name, instance)

    def save(self, commit=True, user=None):
        """Save both forms and attach the user to the profile."""
        instances = self._combine('save', call=True, ignore_missing=True, call_kwargs={'commit': False})

        user.first_name = instances['user'].first_name
        user.last_name  = instances['user'].last_name
        instances['user'] = user

        instances['profile'].user = user
        instances['profile'].save()
        instances['user'].save()
        return instances
