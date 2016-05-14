from django import template
from ..models import Event

register = template.Library()


@register.assignment_tag()
def participation(ev, us):
	"""Check if user is contain in event"""
	return bool(Event.objects.filter(id__exact = ev.id).filter(participation__user = us))
