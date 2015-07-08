from django.conf.urls     		import patterns, url, include
from django.views.generic 		import TemplateView
from django.conf.urls.i18n 		import i18n_patterns
from django.utils.translation	import ugettext_lazy 			as _

urlpatterns = patterns('',

	url(r'^$',        			'core.views.home',                                   	name = 'home'),
	# Agenda
	url(r'^agenda$',  			TemplateView.as_view(template_name = 'agenda.html'), 	name = 'agenda'),
    # HQ
    url(r'^hq$',      			TemplateView.as_view(template_name = 'hq.html'),     	name = 'hq'),
    # Carte
    url(r'^map$',    			'core.views.map',                                    	name = 'map'),
    # Amis
	url(r'^friends$', 			'core.views.friends',                                	name = 'friends'),

	url(_(r'^en/'), include(patterns('',

	    # Agenda
	    url(_(r'^agenda$'),  	TemplateView.as_view(template_name = 'agenda.html'), 	name = 'agenda'),
	    # HQ
	    url(_(r'^hq$'),      	TemplateView.as_view(template_name = 'hq.html'),     	name = 'hq'),
	    # Carte
	    url(_(r'^map$'),    	'core.views.map',                                    	name = 'map'),
	    # Amis
		url(_(r'^friends$'), 	'core.views.friends',                                	name = 'friends'),
	))),
)