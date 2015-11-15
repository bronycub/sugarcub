from django                      import forms
from .                           import models
from django.contrib.auth.models  import User
from django.contrib.auth.forms   import AuthenticationForm as BaseAuthenticationForm
from bootstrap3_datetime.widgets import DateTimePicker
from django.utils.translation    import ugettext_lazy as _


class UserForm(forms.ModelForm):

    class Meta:
        model  = User
        fields = ['first_name', 'last_name']


class UserPonyForm(forms.ModelForm):

    class Meta:
        model = models.UserPony
        fields = ['pony', 'message']

    def __init__(self, *args, **kwargs):
        super(UserPonyForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'placeholder':
            _('Exemple : Pony is best pegasus/pony/unicorn!')
        })


class ProfileForm(forms.ModelForm):

    birthday = forms.DateTimeField(
        widget=DateTimePicker(options={"format": "DD/MM/YYYY"}),
        label = _("Birthday")
    )

    class Meta:
        model   = models.Profile
        exclude = ['user', 'enabled', 'address_latitude', 'address_longitude']
        labels = {
            "bio": _("Biography"),
            "phone": _("Phone"),
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


class AuthenticationForm(BaseAuthenticationForm):

    username = forms.CharField(max_length=256, label = _('Username or email'))
