from django.conf.urls         import url
from django.views.generic     import TemplateView
from django.utils.translation import ugettext_lazy as _
from .                        import views


urlpatterns = [
    url(_(r'^members$'),  views.members,                    name = 'members'),
    url(_(r'^profile$'),  views.profile,                    name = 'profile'),
    url(_(r'^register$'), views.RegistrationView.as_view(), name = 'registration_register'),
    url(_(r'^register/informations$'),
        TemplateView.as_view(template_name = 'registration/informations.html'),  name = 'pre_register'),
]
