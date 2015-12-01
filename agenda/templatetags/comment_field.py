from django import template
from ..forms import CommentForm


register = template.Library()


@register.simple_tag(takes_context = True)
def comment_form(context, form = CommentForm()):
    t = template.loader.get_template('form/comment_form.html')
    context['comment_form'] = form
    return t.render(context)
