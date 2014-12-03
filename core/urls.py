from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$',        'core.views.home',    name = 'home'),
    url(r'^agenda$',  'core.views.home',    name = 'agenda'),
    url(r'^map$',     'core.views.map',     name = 'map'),
    url(r'^friends$', 'core.views.friends', name = 'friends'),
)

