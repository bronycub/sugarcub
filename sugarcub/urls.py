from django.conf.urls         import include, url, i18n
from django.contrib           import admin
from django.conf              import settings
from django.conf.urls.static  import static
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth      import views as auth_views
from users.forms              import AuthenticationForm


urls = [
    url(_(r'admin/doc/'), include('django.contrib.admindocs.urls')),
    url(_(r'admin/'),     include(admin.site.urls)),

    url(_(r'bbbff/'),     include('bbbff.urls',  namespace='bbbff')),
    url(_(r'agenda/'),    include('agenda.urls', namespace='agenda')),
    url(r'',              include('users.urls',  namespace='users')),
    url(r'',              include('core.urls',   namespace='core')),

    url(r'^login/$',
        auth_views.login,
        {
            'template_name': 'registration/login.html',
            'authentication_form': AuthenticationForm
        },
        name='auth_login'),
    url(r'',              include('registration.backends.default.urls')),
]


urlpatterns = i18n.i18n_patterns(*urls)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
