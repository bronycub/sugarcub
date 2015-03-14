from django.conf.urls import patterns, include, url
from .views import RegistrationView

urlpatterns = patterns('',
    url(r'^members$', 'users.views.members', name = 'members'),
    url(r'^profile$',  'users.views.profile', name = 'profile'),
    url(r'^register/$',
        RegistrationView.as_view(),
        name='registration_register'
    ),
)

