from django                   import forms
from .                        import models
from django.utils.translation import ugettext_lazy as _


class EventForm(forms.ModelForm):

    class Meta:
        model  = models.Event
        exclude = ['author']
        labels = {
            "title": _("Title"),
            "description": _("Description"),
            "address": _("Address of the event"),
            "date_begin": _("Start date"),
            "date_end": _("End date"),
            "event_enabled": _("Means of contact")
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model  = models.Comment
        fields = ['text']
