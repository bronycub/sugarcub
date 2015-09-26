from django import forms
from .      import models


class EventForm(forms.ModelForm):

    class Meta:
        model  = models.Event
        exclude = ['author']


class CommentForm(forms.ModelForm):

    class Meta:
        model  = models.Comment
        fields = ['text']
