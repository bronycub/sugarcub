from django.conf.urls         import url
from .                        import views, models
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    url(
        regex = r'^$',
        view  = views.medias_category,
        name  = 'medias_category',
    ),
]
