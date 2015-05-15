from   .   import models
import ics


def import_calendar(calendar):
    ''' Insert in database the events from a ics calendar instance '''

    for ics_event in calendar:
        models.Event.objects.create(ics_import = ics_event)


def export_calendar():
    ''' Create an ics calendar from the content of the database '''

    return ics.Calendar(
        events = [event.to_ics_event() for event in models.Event.objects.all()]
    )
