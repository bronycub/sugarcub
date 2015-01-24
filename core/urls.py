from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$',        'core.views.home',    name = 'home'),

    url(r'^members$', 'core.views.members', name = 'members'),
    url(r'^agenda$',  'core.views.home',    name = 'agenda'),
    url(r'^map$',     'core.views.map',     name = 'map'),
    url(r'^friends$', 'core.views.friends', name = 'friends'),

	url(r'^login$',   'django.contrib.auth.views.login',  {'template_name': 'auth/login.html',  'current_app': 'core'},    name = 'login'),
	url(r'^logout$',  'django.contrib.auth.views.logout', {'template_name': 'auth/logout.html', 'next_page': 'core:home'}, name = 'logout'),
	url(r'^signup$',  'core.views.signup',  name = 'signup'),

	url(r'^signup_success$',  'core.views.signup_success',  name = 'signup_success'),
)

