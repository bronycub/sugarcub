from django.test import TestCase
from utils.tests import *
from .           import models
from model_mommy import mommy


class UsersModelsTest(TestCase):

    def test_name_quote(self):
        quote    = mommy.make(models.Quote, quote = 'test')
        quote.full_clean()

        assert 'test' == quote.__str__()

    def test_name_friend(self):
        friend = mommy.make(models.Friend, name = 'test')
        friend.full_clean()

        assert 'test' == friend.__str__()

    def test_name_event(self):
        event = mommy.make(models.Event, title = 'test')
        event.full_clean()

        assert 'test' == event.__str__()
