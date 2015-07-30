from django.conf.urls           import patterns, url, include
from django.views.generic       import TemplateView
from .views                     import RegistrationView
from django.utils.translation   import ugettext_lazy             as _

urlpatterns = patterns('',
    # Membres
    url(r'^members$', 'users.views.members', name = 'members'),
    # Profil
    url(r'^profile$', 'users.views.profile', name = 'profile'),
    # Inscription
    url(r'^register/$', RegistrationView.as_view(), name='registration_register'),
    # Information
    url(r'^register/informations$',
        TemplateView.as_view(template_name = 'registration/informations.html'),  name = 'pre_register'),

    url(_(r'^en/'), include(patterns('',
        # Membres
        url(_(r'^members$'), 'users.views.members', name = 'members'),
        # Profil
        url(_(r'^profile$'), 'users.views.profile', name = 'profile'),
        # Inscription
        url(_(r'^register/$'), RegistrationView.as_view(), name='registration_register'),
        # Information
        url(_(r'^register/informations$'),
            TemplateView.as_view(template_name = 'registration/informations.html'),  name = 'pre_register'),
    ))),
)
