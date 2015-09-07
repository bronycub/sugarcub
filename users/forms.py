from django                         import forms
from registration.forms             import RegistrationFormUniqueEmail
from multiform                      import MultiModelForm, InvalidArgument
from .models                        import Profile
from django.contrib.auth.models     import User
from django.utils.translation       import ugettext_lazy                    as _
from xml.dom                        import minidom
import urllib.request
import xml.etree.ElementTree            as ET


class UserForm(forms.ModelForm):

    class Meta:
        model  = User
        fields = ['first_name', 'last_name']


class ProfileForm(forms.ModelForm):

    class Meta:
        model   = Profile
        exclude = ['user', 'enabled', 'address_latitude', 'address_longitude']
        labels = {
            "bio": _("Biography"),
            "phone": _("Phone"),
            "birthday": _("Birthday"),
            "address": _("Address"),
            "city": _("City"),
            "postal_code": _("Postal code"),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['bio'].widget.attrs.update({
                'placeholder': 
                _('Write about yourself! how you discover My Little Pony or BronyCUB, what you like and dislike...')
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

    def get_gps_position(self, address, city):
        """Get and return longitute and latitude"""

        address = address.replace(" ", "+")
        city = city.replace(" ", "+")

        nominatim_query = "https://nominatim.openstreetmap.org/search?q=" + address + ",+" + city + "&format=xml"
        print(nominatim_query)
        doc = urllib.request.urlopen(nominatim_query)
        tree = ET.parse(doc)
        root = tree.getroot()
        return float(root[0].get("lat", default=None)), float(root[0].get("lon", default=None))

    def save(self, commit=True, user=None):
        """Save both forms and attach the user to the profile."""
        instances = self._combine('save', call=True, ignore_missing=True, call_kwargs={'commit': False})

        user.first_name = instances['user'].first_name
        user.last_name  = instances['user'].last_name
        instances['user'] = user

        instances['profile'].address_latitude, instances['profile'].address_longitude = self.get_gps_position(instances['profile'].address, instances['profile'].city)

        print(instances['profile'].address_latitude, instances['profile'].address_longitude)

        instances['profile'].user = user
        instances['profile'].save()
        instances['user'].save()

        return instances
