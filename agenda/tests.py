from   django.test import TestCase
from   .           import views, models
from   model_mommy import mommy
import unittest

class AgendaViewsTest(TestCase):

    @unittest.skipIf(True, 'not implemented')
    def test_index(self):
        self.fail('todo')

    @unittest.skipIf(True, 'not implemented')
    def test_create(self):
        self.fail('todo')


class AgendaModelsTest(TestCase):

    def test_name_event(self):
        event = mommy.make(models.Event,
            title = "Picnic at Flutter's",
        )
        event.full_clean()

        self.assertEquals("Picnic at Flutter's", event.__unicode__())

    def test_name_comment(self):
        comment = mommy.make(models.Comment,
            text = "Hope Angel doesn't make a scene again …",
        )
        comment.full_clean()

        self.assertEquals( "Hope Angel doesn't make a scene again …", comment.__unicode__())


