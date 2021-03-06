from django.shortcuts               import render
from django.core.urlresolvers       import reverse_lazy
from django.views.generic.edit      import CreateView, UpdateView
from .                              import models, forms, utils
from .forms                         import EventForm, CommentForm, ParticipationForm
from el_pagination.views            import AjaxListView
from django.http                    import HttpResponse
from django.shortcuts               import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators        import method_decorator
import json


class CommentAjaxListView(AjaxListView):

    form_class = forms.CommentForm

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
        instance.save()
        utils.send_new_event_notification.delay(instance.id)
        return super().form_valid(form)


class UpdateEventView(UpdateView):

    model         = models.Event
    form_class    = forms.EventForm
    success_url   = reverse_lazy('agenda:list')
    template_name = 'agenda/event_form.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def post_comment(request):

    if request.POST:
        captcha = CommentForm(request.POST)
        if request.user.is_authenticated():
            event = models.Event.objects.get(pk = request.POST.get('event'))
            comment = models.Comment(
                author = request.user,
                text = request.POST.get('text'),
                event = event
            )
            comment.save()

        else:
            if captcha.is_valid():
                event = models.Event.objects.get(pk = request.POST.get('event'))
                comment = models.Comment(
                    pseudo = request.POST.get('pseudo'),
                    text = request.POST.get('text'),
                    event = event
                )
                comment.save()
            else:
                return HttpResponse(json.dumps(captcha.errors), status=400)

        return HttpResponse('success')


def participate(request):

    if request.method == 'POST':
        captcha = ParticipationForm(request.POST)
        if request.user.is_authenticated():
            event = models.Event.objects.get(pk = request.POST.get('event'))
            participation = models.Participation(
                user = request.user,
                event = event
            )
            try:
                participation.save()
            except:
                return HttpResponse(json.dumps(captcha.errors), status=400)

        else:
            if captcha.is_valid():
                event = models.Event.objects.get(pk = request.POST.get('event'))
                participation = models.Participation(
                    pseudo = request.POST.get('pseudo'),
                    event = event,
                    contact = request.POST.get('contact'),
                )
                try:
                    participation.save()
                except:
                    return HttpResponse(json.dumps(captcha.errors), status=400)

        return HttpResponse('success')

    return redirect('agenda:list')


def ics_export(request):
    calendar = str(utils.export_calendar())
    response = HttpResponse(calendar, content_type = 'text/calendar; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=agenda.ics'
    response['Content-Lenght'] = len(calendar)
    return response


def update_event(request, event_id):
    try:
        event = models.Event.objects.get(id = event_id)
    except:
        return redirect('agenda:list')

    if event.author.id == request.user.id:
        if request.method == 'POST':

            form = EventForm(request.POST, request.FILES, instance = event)

            if form.is_valid():
                form.save()

                return redirect('agenda:list')

        else:
            form = EventForm(instance = event)

        return render(request, 'agenda/event_update_form.html', {
            'event':   event,
            'form':    form,
        })

    else:
        return redirect('agenda:list')
