from django.contrib.auth          import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.core.mail             import mail_admins
from django.utils.translation     import ugettext as _
from django.template.loader       import render_to_string
from celery                       import shared_task
from .                            import models


class EmailModelBackend(ModelBackend):
    ''' Authenticate user by email '''

    def authenticate(self, username = None, password = None):
        user_model = get_user_model()

        try:
            user = user_model.objects.get(email = username)
            if user.check_password(password):
                return user
            else:
                return None
        except user_model.DoesNotExist:
            return None


@shared_task
def send_admin_registration_notification(profile_id):
    profile = models.Profile.objects.get(pk = profile_id)

    mail_admins(
        _('Nouvelle inscription'),
        html_message = render_to_string('registration/email-admin-notification.html', {'profile': profile})
    )
