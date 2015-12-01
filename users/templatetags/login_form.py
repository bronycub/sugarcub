from django import template
from ..forms import AuthenticationForm


register = template.Library()


@register.simple_tag(takes_context = True)
def login_form(context, form = AuthenticationForm()):
    t = template.loader.get_template('registration/forms/login.html')
    context['authentication_form'] = form
    return t.render(context)
