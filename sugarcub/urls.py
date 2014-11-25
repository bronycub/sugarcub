from   django.conf.urls import patterns, include, url
from   django.contrib   import admin

urlpatterns = patterns('',
    url(r'^admin/',   include(admin.site.urls)),

    url(r'^users/',   include('users.urls')),
    url(r'^bbbff/',   include('bbbff.urls')),

    url(r'^$',        'sugarcub.views.home',    name='home'),
    url(r'^agenda$',  'sugarcub.views.home',    name='agenda'),
    url(r'^map$',     'sugarcub.views.maps',    name='map'),
    url(r'^friends$', 'sugarcub.views.friends', name='friends'),
)

