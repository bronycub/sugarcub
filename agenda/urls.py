from django.conf.urls         import patterns, url
from .                        import views, models
from endless_pagination.views import AjaxListView


urlpatterns = patterns('',
    url(
        regex = r'^$',
        view  = AjaxListView.as_view(model = models.Event),
        name  = 'list',
    ),
    url(
        regex = r'^(?P<event_id>[0-9]+)/comments$',
        view  = views.CommentAjaxListView.as_view(),
        name  = 'comment_list',
    ),
    url(
        regex = r'^ics$',
        view  = views.ics_export,
        name  = 'ics_export',
    ),
)
