from django import forms
from .      import validators


class UrlField(forms.CharField):
    default_validators = [validators.UrlValidator()]
