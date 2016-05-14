from django.conf import settings


def custom_fields(request):
    ''' Provides a list of fields custom for each collective '''

    return {'collective_name': settings.COLLECTIVE_NAME}


def mailing_list(request):
    ''' Provides the mailing list address '''

    return {'mailing_list': settings.DEFAULT_FROM_EMAIL}
