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
            "date_begin": _("Date begin"),
            "date_end": _("Date end"),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model  = models.Comment
        fields = ['text']
