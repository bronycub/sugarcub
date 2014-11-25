from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$',        'lists.views.home', name = 'home'),
    url(r'^agenda$',  'lists.views.home', name = 'agenda'),
    url(r'^map$',     'lists.views.home', name = 'map'),
    url(r'^friends$', 'lists.views.home', name = 'friends'),
)

