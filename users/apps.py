from django.apps              import AppConfig as _AppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(_AppConfig):
    name         = 'users'
    verbose_name = _('Users')
