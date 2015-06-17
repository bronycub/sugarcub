from   django.test                import TestCase
from   utils.tests                import *
from   django.contrib.auth.models import User
from   .                          import models
from   model_mommy                import mommy
from   datetime                   import datetime, timedelta
import ics


class AgendaModelsTest(TestCase):

    def test_event_ordering(self):
        older_event = mommy.make(models.Event,
            date_begin = datetime.now() - timedelta(hours = 2),
            date_end   = datetime.now() - timedelta(hours = 1),
        )
        newer_event = mommy.make(models.Event,
            date_begin = datetime.now() - timedelta(hours = 2),
            date_end   = datetime.now(),
        )
        newest_event = mommy.make(models.Event,
            date_begin = datetime.now(),
            date_end   = datetime.now(),
        )

        assert newest_event == models.Event.objects.all()[0]
        assert newer_event  == models.Event.objects.all()[1]
        assert older_event  == models.Event.objects.all()[2]
        assert 3            == models.Event.objects.count()

    def test_name_event(self):
        event = mommy.make(models.Event,
            title = "Picnic at Flutter's",
        )

        self.assertEquals("Picnic at Flutter's", event.__str__())

    def test_comment_ordering(self):
        older_comment = mommy.make(models.Comment, date = datetime.now() - timedelta(hours = 1))
        newer_comment = mommy.make(models.Comment, date = datetime.now())

        assert newer_comment == models.Comment.objects.all()[0]
        assert older_comment == models.Comment.objects.all()[1]
        assert 2             == models.Event.objects.count()

    def test_name_comment(self):
        comment = mommy.make(models.Comment,
            text = "Hope Angel doesn't make a scene again …",
        )

        assert "Hope Angel doesn't make a scene again …" == comment.__str__()

    def test_name_participation_user(self):
        user = mommy.make(User, username = 'test')
        event = mommy.make(models.Event, title = 'Test')
        participation = mommy.make(models.Participation, event = event, user = user)

        assert 'test Test' == participation.__str__()
        assert user        == participation.author()

    def test_name_participation_pseudo(self):
        event = mommy.make(models.Event, title = 'Test')
        participation = mommy.make(models.Participation, event = event, pseudo = 'test')

        assert 'test Test' == participation.__str__()
        assert 'test'      == participation.author()

    def test_from_ics(self):
        now   = datetime.now()
        event = mommy.make(models.Event,
            title       = 'name',
            date_begin  = now,
            date_end    = now + timedelta(days = 1, hours = 1),
            description = 'description',
        )
        ics_event = ics.Event(
            name        = 'name',
            begin       = now,
            end         = now + timedelta(days = 1, hours = 1),
            description = 'description',
        )

        event_imported = models.Event.objects.create(
            author     = event.author,
            ics_import = ics_event,
        )
        assert objects_contain_same_data(event, event_imported)

    def test_to_ics(self):
        now   = datetime.now()
        event = mommy.make(models.Event,
            title       = 'name',
            date_begin  = now,
            date_end    = now + timedelta(days = 1, hours = 1),
            description = 'description',
        )
        ics_event = ics.Event(
            name        = 'name',
            begin       = now,
            end         = now + timedelta(days = 1, hours = 1),
            description = 'description',
        )

        assert objects_contain_same_data(ics_event, event.to_ics_event())

    def test_from_to_event(self):
        now   = datetime.now()
        event = mommy.make(models.Event,
            title       = 'name',
            date_begin  = now,
            date_end    = now + timedelta(days = 1, hours = 1),
            description = 'description',
        )

        ics_event = event.to_ics_event()
        assert objects_contain_same_data(
            event,
            models.Event.objects.create(
                author     = event.author,
                ics_import = ics_event,
            )
        )

    def test_from_to_ics(self):
        now   = datetime.now()
        ics_event = ics.Event(
            name        = 'name',
            begin       = now,
            end         = now + timedelta(days = 1, hours = 1),
            description = 'description',
        )

        event_imported = models.Event.objects.create(
            author = mommy.make(User),
            ics_import = ics_event,
        )
        assert objects_contain_same_data(ics_event, event_imported.to_ics_event())


def objects_contain_same_data(expected, given):
    assert expected.__class__ == given.__class__
    print(expected.__dict__)
    for i in expected.__dict__.keys():
        if not (i == 'pk' or i == 'id' or i == 'uid' or i.startswith('_')):
            assert getattr(expected, i) == getattr(given, i)

    return True
