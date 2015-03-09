from   django.conf.urls import patterns, include, url
from   django.contrib   import admin

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/',     include(admin.site.urls)),

    url(r'^bbbff/',     include('bbbff.urls', namespace='bbbff')),

    url(r'^',           include('users.urls', namespace='users')),
    url(r'^',           include('core.urls', namespace='core')),
)

