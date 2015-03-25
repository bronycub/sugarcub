from django.conf.urls	  import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$',		  'core.views.home',									name = 'home'),

    url(r'^agenda$',  TemplateView.as_view(template_name = 'agenda.html'),	name = 'agenda'),
    url(r'^hq$',	  TemplateView.as_view(template_name = 'hq.html'),		name = 'hq'),
    url(r'^map$',	  'core.views.map',										name = 'map'),
    url(r'^friends$', 'core.views.friends',									name = 'friends'),
)

