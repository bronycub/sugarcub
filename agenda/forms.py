from django                      import forms
from .                           import models
from bootstrap3_datetime.widgets import DateTimePicker
from django.utils.translation    import ugettext_lazy as _
from captcha.fields              import CaptchaField


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'placeholder':
            _('Explain the event, add as much information you can : time, localisation '
                ', if people need stuff... the more information the better!')
        })


class CommentForm(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:
        model  = models.Comment
        fields = ['text', 'pseudo']


class ParticipationForm(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = models.Participation
        fields = ['pseudo', 'contact']
