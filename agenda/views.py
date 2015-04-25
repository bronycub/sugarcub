from django.shortcuts         import render
from .                        import models
from endless_pagination.views import AjaxListView

class CommentAjaxListView(AjaxListView):

    def get_queryset(self):
        return models.Comment.objects.filter(event = self.kwargs['event_id'])
