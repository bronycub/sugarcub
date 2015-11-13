from django                      import forms
from registration.forms          import RegistrationFormUniqueEmail
from multiform                   import MultiModelForm, InvalidArgument
from .models                     import Profile
from django.contrib.auth.models  import User
from bootstrap3_datetime.widgets import DateTimePicker
from django.utils.translation    import ugettext_lazy as _


class UserForm(forms.ModelForm):

    class Meta:
        model  = User
        fields = ['first_name', 'last_name']


class UserPonyForm(forms.ModelForm):

    class Meta:
        model = UserPony
        fields = ['pony', 'message']

    def __init__(self, *args, **kwargs):
        super(UserPonyForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'placeholder':
            _('Exemple : Pony is best pegasus/pony/unicorn!')
        })


class ProfileForm(forms.ModelForm):

    birthday = forms.DateTimeField(widget=DateTimePicker(options={"format": "DD/MM/YYYY"}), label = _("Birthday"))

    class Meta:
        model   = Profile
        exclude = ['user', 'enabled', 'address_latitude', 'address_longitude']
        labels = {
            "bio": _("Biography"),
            "phone": _("Phone"),
            # "birthday": _("Birthday"),
            "address": _("Address"),
            "city": _("City"),
            "postal_code": _("Postal code"),
            "name_enabled": _("Hide my firstname and lastname"),
            "phone_enabled": _("Hide my phone number"),
            "birthday_enabled": _("Hide my birthday"),
            "address_enabled": _("Hide my address"),
            "mail_enabled": _("Hide my email"),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs.update({'placeholder':
            _('Write about yourself! how you discover My Little Pony or BronyCUB, '
                'what you like and dislike...')
        })


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
