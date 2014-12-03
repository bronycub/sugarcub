from   django.conf.urls import patterns, include, url
from   django.contrib   import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^users/', include('users.urls')),
    url(r'^bbbff/', include('bbbff.urls')),

	url(r'^',      include('core.urls')),
)

