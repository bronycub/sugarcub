from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^members$', 'users.views.members', name = 'members'),

    url(r'^login$',   'django.contrib.auth.views.login',  {'template_name': 'auth/login.html',  'current_app': 'core'},    name = 'login'),
    url(r'^logout$',  'django.contrib.auth.views.logout', {'template_name': 'auth/logout.html', 'next_page': 'core:home'}, name = 'logout'),
    url(r'^signup$',  'users.views.signup',  name = 'signup'),

    url(r'^signup_success$',  'users.views.signup_success',  name = 'signup_success'),
)

