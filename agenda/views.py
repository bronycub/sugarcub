from django.shortcuts import render
from .                import models

def event_list(request):

    events = models.Event.objects.all()

    if request.is_ajax():
        template = 'event_list_page.html'
    else:
        template = 'event_list.html'

    return render(request, template, {
        'events': events,
    })

def comment_list(request, event_id):

    comments = models.Comment.objects.filter(event = event_id)

    if request.is_ajax():
        template = 'comment_list_page.html'
    else:
        template = 'comment_list.html'

    return render(request,template, {
        'comments': comments,
    })
