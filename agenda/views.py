from django.core.urlresolvers       import reverse_lazy
from django.views.generic.edit      import CreateView, UpdateView
from .                              import models, forms, utils
from endless_pagination.views       import AjaxListView
from django.http                    import HttpResponse
from django.shortcuts               import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators        import method_decorator


class CommentAjaxListView(AjaxListView):

    def get_queryset(self):
        return models.Comment.objects.filter(event = self.kwargs['event_id'])


class CreateEventView(CreateView):

    form_class    = forms.EventForm
    success_url   = reverse_lazy('agenda:list')
    template_name = 'agenda/event_form.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        instance = form.save(commit = False)
        instance.author = self.request.user
        return super().form_valid(form)


class UpdateEventView(UpdateView):

    model         = models.Event
    form_class    = forms.EventForm
    success_url   = reverse_lazy('agenda:list')
    template_name = 'agenda/event_form.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@login_required
def post_comment(request):

    if request.method == 'POST':
        event = models.Event.objects.get(pk = request.POST.get('event'))
        comment = models.Comment(
            author = request.user,
            text = request.POST.get('text'),
            event = event
        )
        comment.save()

        return HttpResponse('success')

    return redirect('agenda:list')


def ics_export(request):
    calendar = str(utils.export_calendar())
    response = HttpResponse(calendar, content_type = 'text/calendar; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=agenda.ics'
    response['Content-Lenght'] = len(calendar)
    return response
