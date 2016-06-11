from django import template
import datetime
from django.utils import timezone


register = template.Library()


@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

@register.filter
def hours_ago(time, hours):
    return time + datetime.timedelta(hours=hours) < timezone.now()
