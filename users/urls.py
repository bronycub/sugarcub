from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^members$', 'users.views.members', name = 'members'),
    url(r'^profile$',  'users.views.profile', name = 'profile'),
)

