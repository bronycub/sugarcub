from .                        import models, utils
from endless_pagination.views import AjaxListView
from django.http              import HttpResponse


class CommentAjaxListView(AjaxListView):

    def get_queryset(self):
        return models.Comment.objects.filter(event = self.kwargs['event_id'])


def ics_export(request):
    calendar = str(utils.export_calendar())
    response = HttpResponse(calendar, content_type = 'text/calendar; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=agenda.ics'
    response['Content-Lenght'] = len(calendar)
    return response


def ics_import(request):
    pass
