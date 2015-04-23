from   model_mommy                import mommy
from   django.contrib.auth.models import User
from   django.core.urlresolvers   import reverse
from   django_webtest             import WebTest
from   agenda                     import models
import datetime
import unittest
import re

class AgendaTest(WebTest):

    def setUp(self):
        events = mommy.make(model.Event,
            _quantity = 20,
        )

    @unittest.skipIf(True, 'not implemented')
    def test_list_events(self):
        '''Test that you can see and navigate the list of events'''
        # You can go to the agenda page
        page = self.app.get(reverse('agenda:index'))

        # You can see all the upcoming events or the 10 most recent events
        # You can navigate the older events with the pagination buttons
        # You can search for an event

        self.fail('TODO : Write the functionalities and tests')

    @unittest.skipIf(True, 'not implemented')
    def test_comments(self):
        '''Test that you can see and navigate all comments and add one'''
        page = self.app.get(reverse('agenda:index'))

        # You can show the comments for an event
        # You see older comments when going back in the history
        # You can add a comment addee it appear at the top

        self.fail('TODO : Write the functionalities and tests')

    @unittest.skipIf(True, 'not implemented')
    def test_can_participate(self):
        '''Test that you can participate and unparticipate to an event'''
        page = self.app.get(reverse('agenda:index'))

        # You can click the participate button
        # You can click the cancel participation button

        self.fail('TODO : Write the functionalities and tests')

    @unittest.skipIf(True, 'not implemented')
    def test_create_event(self):
        '''Test that you can create an event'''
        # You can go to the create an event page
        # The event appears in the list

        self.fail('TODO : Write the functionalities and tests')
