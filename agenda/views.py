from django.core.urlresolvers  import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .                         import models,     forms, utils
from endless_pagination.views  import AjaxListView
from django.http               import HttpResponse
from django.shortcuts          import redirect


class CommentAjaxListView(AjaxListView):

    def get_queryset(self):
        return models.Comment.objects.filter(event = self.kwargs['event_id'])


class CreateEventView(CreateView):

    form_class    = forms.EventForm
    success_url   = reverse_lazy('agenda:list')
    template_name = 'agenda/event_form.html'

    def form_valid(self, form):
        instance = form.save(commit = False)
        instance.author = self.request.user
        return super().form_valid(form)


class UpdateEventView(UpdateView):

    model         = models.Event
    form_class    = forms.EventForm
    success_url   = reverse_lazy('agenda:list')
    template_name = 'agenda/event_form.html'


def post_comment(request):

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('agenda:list')


def ics_export(request):
    calendar = str(utils.export_calendar())
    response = HttpResponse(calendar, content_type = 'text/calendar; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=agenda.ics'
    response['Content-Lenght'] = len(calendar)
    return response
