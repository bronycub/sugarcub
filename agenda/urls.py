from django.conf.urls         import url
from .                        import views, models
from endless_pagination.views import AjaxListView
from django.utils.translation import ugettext_lazy as _


urlpatterns = [
    url(
        regex = r'^$',
        view  = AjaxListView.as_view(model = models.Event),
        name  = 'list',
    ),
    url(
        regex = _(r'^(?P<event_id>[0-9]+)/comments$'),
        view  = views.CommentAjaxListView.as_view(),
        name  = 'comment_list',
    ),
    url(
        regex = _(r'^event$'),
        view  = views.CreateEventView.as_view(),
        name  = 'event',
    ),
    url(
        regex = _(r'^event/(?P<pk>[\d]+)$'),
        view  = views.UpdateEventView.as_view(),
        name  = 'event',
    ),
    url(
        regex = _(r'^comment$'),
        view  = views.post_comment,
        name  = 'comment',
    ),
    url(
        regex = _(r'^participations$'),
        view  = views.participate,
        name  = 'participate',
    ),
    url(
        regex = _(r'^ics$'),
        view  = views.ics_export,
        name  = 'ics_export',
    ),
]
