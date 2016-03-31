from django                      import forms
from .                           import models
from django.contrib.auth.models  import User
from bootstrap3_datetime.widgets import DateTimePicker
from django.utils.translation    import ugettext_lazy as _
from multiform                   import MultiModelForm, InvalidArgument
from registration.forms          import RegistrationFormUniqueEmail
from django.contrib.auth.forms   import AuthenticationForm as _AuthenticationForm


class UserForm(forms.ModelForm):

    class Meta:
        model  = User
        fields = ['first_name', 'last_name']


class UserPonyForm(forms.ModelForm):

    class Meta:
        model = models.UserPony
        fields = ['pony', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'placeholder':
            _('Exemple : Pony is best pegasus/pony/unicorn!')
        })


class ProfileForm(forms.ModelForm):

    birthday = forms.DateTimeField(
        widget = DateTimePicker(
            options = {
                'format': 'DD/MM/YYYY',
                'viewMode': 'years',
            }
        ),
        label = _("Birthday")
    )

    class Meta:
        model   = models.Profile
        fields = [
            'bio', 'avatar', 'phone', 'birthday', 'address', 'city', 'postal_code',
            'name_enabled', 'phone_enabled', 'birthday_enabled', 'address_enabled', 'mail_enabled'
        ]
        labels = {
            'bio': _('Biography'),
            'phone': _('Phone'),
            'address': _('Address'),
            'city': _('City'),
            'postal_code': _('Postal code'),
            'name_enabled': _('Show my firstname and lastname (When hidden only your pseudo will be visible)'),
            'phone_enabled': _('Show my phone number (When hidden your will only be rechable by email'),
            'birthday_enabled': _('Show my birthday (When hidden nobody will know your age or your birthday)'),
            'address_enabled': _('Show my address (When hidde nyou will not appear on the members map'),
            'mail_enabled': _('Show my email'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        return super().dispatch_init_instance(name, instance)

    def save(self, commit=True, user=None):
        ''' Save both forms and attach the user to the profile. '''
        instances = self._combine('save', call=True, ignore_missing=True, call_kwargs={'commit': False})

        user.first_name = instances['user'].first_name
        user.last_name  = instances['user'].last_name
        instances['user'] = user

        instances['profile'].user = user
        instances['profile'].save()
        instances['user'].save()

        return instances


class AuthenticationForm(_AuthenticationForm):

    username = forms.CharField(max_length=256, label = _('Username or email'))
