from django import template

register = template.Library()


@register.assignment_tag()
def participation(ev, us):
	"""Check if user is contain in event"""
	return bool(ev.filter(participation__user = us))