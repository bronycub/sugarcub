from django.conf import settings
from .models     import Event


def custom_fields(request):
    ''' Provides a list of fields custom for each collective '''
    return {'collective_name': settings.COLLECTIVE_NAME}


def humanitarian_actions(request):
    ''' Provides the next humanitarian actions for the footer '''
    return {'next_humanitarian_action': Event.objects.first()}


def mailing_list(request):
    ''' Provides the mailing list address '''
    return {'mailing_list': settings.DEFAULT_FROM_EMAIL}
