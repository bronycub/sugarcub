from django.conf.urls         import url
from django.views.generic     import TemplateView
from .views                   import RegistrationView
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    url(_(r'^members$'),   'users.views.members',      name = 'members'),
    url(_(r'^profile$'),   'users.views.profile',      name = 'profile'),
    url(_(r'^register$'), RegistrationView.as_view(), name='registration_register'),
    url(_(r'^register/informations$'),
        TemplateView.as_view(template_name = 'registration/informations.html'),  name = 'pre_register'),
]
