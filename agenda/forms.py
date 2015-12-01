from django                      import forms
from .                           import models
from bootstrap3_datetime.widgets import DateTimePicker
from django.utils.translation    import ugettext_lazy as _


class EventForm(forms.ModelForm):

    date_begin = forms.DateTimeField(
        widget = DateTimePicker(
            options = {
                'format': 'DD/MM/YYYY HH:mm',
                'inline': True,
            }
        ),
        label = _('Start date and hour')
    )
    date_end = forms.DateTimeField(
        widget = DateTimePicker(
            options = {
                'format': 'DD/MM/YYYY HH:mm',
                'inline': True,
            }
        ),
        label = _('End date and hour')
    )

    class Meta:
        model  = models.Event
        exclude = ['author']
        labels = {
            'title':         _('Title'),
            'description':   _('Description'),
            'address':       _('Address of the event'),
            'event_enabled': _('Means of contact')
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model  = models.Comment
        fields = ['text']
