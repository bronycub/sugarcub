from django.conf.urls	  import patterns, include, url
from django.views.generic import TemplateView
from .views				  import RegistrationView

urlpatterns = patterns('',
    url(r'^members$', 'users.views.members', name = 'members'),
    url(r'^profile$',  'users.views.profile', name = 'profile'),
    url(r'^register/$',
        RegistrationView.as_view(),
        name='registration_register'
    ),
    url(r'^register/informations$', TemplateView.as_view(template_name = 'registration/informations.html'), name = 'pre_register'),
)

