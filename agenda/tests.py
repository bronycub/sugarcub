from   django.test                import TestCase
from   django.contrib.auth.models import User
from   .                          import views,    models
from   model_mommy                import mommy
from   datetime                   import datetime, timedelta
from   utils.tests                import UnitTestUtilsMixin
import unittest
import ics

class AgendaViewsTest(UnitTestUtilsMixin, TestCase):

    @unittest.skipIf(True, 'not implemented')
    def test_index(self):
        self.fail('todo')

    @unittest.skipIf(True, 'not implemented')
    def test_create(self):
        self.fail('todo')

    def test_export(self):
        self.assert_url_matches_view(views.ics_export, '/agenda/ics', 'agenda:ics_export')


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

        self.assertEquals(newest_event, models.Event.objects.all()[0])
        self.assertEquals(newer_event,  models.Event.objects.all()[1])
        self.assertEquals(older_event,  models.Event.objects.all()[2])
        self.assertEquals(3, models.Event.objects.count())

    def test_name_event(self):
        event = mommy.make(models.Event,
            title = "Picnic at Flutter's",
        )

        self.assertEquals("Picnic at Flutter's", event.__str__())

    def test_comment_ordering(self):
        older_comment = mommy.make(models.Comment, date = datetime.now() - timedelta(hours = 1))
        newer_comment = mommy.make(models.Comment, date = datetime.now())

        self.assertEquals(newer_comment,  models.Comment.objects.all()[0])
        self.assertEquals(older_comment,  models.Comment.objects.all()[1])
        self.assertEquals(2, models.Event.objects.count())

    def test_name_comment(self):
        comment = mommy.make(models.Comment,
            text = "Hope Angel doesn't make a scene again …",
        )

        self.assertEquals( "Hope Angel doesn't make a scene again …", comment.__str__())

    def test_name_participation_user(self):
        user = mommy.make(User, username = 'test')
        event = mommy.make(models.Event, title = 'Test')
        participation = mommy.make(models.Participation, event = event, user = user)

        self.assertEquals('test Test', participation.__str__())
        self.assertEquals(user, participation.author())

    def test_name_participation_pseudo(self):
        event = mommy.make(models.Event, title = 'Test')
        participation = mommy.make(models.Participation, event = event, pseudo = 'test')

        self.assertEquals('test Test', participation.__str__())
        self.assertEquals('test', participation.author())

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

        event_imported = models.Event.objects.create(ics_import = ics_event)
        self.assertEquals(event, event_imported)

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

        self.assertEquals(ics_event, event.to_ics_event())
