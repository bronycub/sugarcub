from django.conf.urls           import url
from django.views.generic       import TemplateView
from django.utils.translation   import ugettext_lazy as _

urlpatterns = [
    url(r'^$',           'core.views.home',                                   name = 'home'),
    url(_(r'^hq$'),      TemplateView.as_view(template_name = 'hq.html'),     name = 'hq'),
    url(_(r'^map$'),     'core.views.map',                                    name = 'map'),
    url(_(r'^friends$'), 'core.views.friends',                                name = 'friends'),
]
