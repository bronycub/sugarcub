from django.conf.urls         import patterns, include, url
from .                        import views, models
from endless_pagination.views import AjaxListView

urlpatterns = patterns('',
    url(
        regex = r'^$',
        view  = AjaxListView.as_view(model = models.Event),
        name  = 'list',
    ),
    url(
        regex = r'^(?P<event_id>[0-9]+)/comments',
        view  = views.CommentAjaxListView.as_view(),
        name  = 'comment_list',
    ),
)

