from django import template
from ..forms import ParticipationForm


register = template.Library()


@register.simple_tag(takes_context = True)
def participation_form(context, form = None, prefix = ''):
    t = template.loader.get_template('form/participation_form.html')
    if not form:
    	form = ParticipationForm(prefix = prefix)

    context['participation_form'] = form
    return t.render(context)
