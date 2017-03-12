from   .                        import models
from   celery                   import shared_task
from   django.core.mail         import mail_admins
from   django.utils.translation import ugettext as _
from   django.template.loader   import render_to_string
import ics


# def import_calendar(calendar):
# 	''' Insert in database the events from a ics calendar instance '''

# 	 for ics_event in calendar:
# 		models.Event.objects.create(author = ?, ics_import = ics_event)


def export_calendar():
    ''' Create an ics calendar from the content of the database '''

    return ics.Calendar(
        events = [event.to_ics_event() for event in models.Event.objects.all()]
    )


@shared_task
def send_admin_event_notification(event_id):
    event = models.Event.objects.get(pk = event_id)

    mail_admins(
        subject      = _('New event'),
        message      = render_to_string('agenda/email-admin-notification.txt',  {'event': event}),
        html_message = render_to_string('agenda/email-admin-notification.html', {'event': event})
    )
