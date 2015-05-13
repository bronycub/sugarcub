from   selenium                       import webdriver
from   utils                          import tests
from   functional_tests.base          import FunctionalTest
from   selenium.webdriver.common.keys import Keys
from   time                           import sleep
import pytest

@pytest.mark.functional
@pytest.mark.selenium
class CoreTest(FunctionalTest):
    '''Test the core functionalitites'''

    def assert_link_text_to_url(self, link, url):
        '''Assert that the link found with the given link name redirects to the given url'''
        self.browser.find_element_by_partial_link_text(link).click()
        self.assertRegex(self.browser.current_url, url)

    @tests.skipNotFinishedYet
    def test_header(self):
        '''Test the header without testing the login/signup, logout, and my account which are tested in users_test'''
        self.browser.get(self.server_url)

        self.browser.current_url

        # You can navigate to the pages linked in the header
        self.assert_link_text_to_url('SugarCUB', '/')
        self.assert_link_text_to_url('Membres',  '/members')
        #self.assert_link_text_to_url('Agenda',   '/agenda')
        #self.assert_link_text_to_url('Medias',   '/bbbff')
        self.assert_link_text_to_url('Carte',    '/map')
        self.assert_link_text_to_url('Amis',     '/friends')

        # You can access external pages (IRC, WebRTC, DJ, Tickets)
        #self.assert_link_text_to_url('Tchat',  'https://kiwiirc.com/client?settings=3ebf3eb7a40c2b03f47b918eb2f7087a')
        #self.assert_link_text_to_url('Visio',  '/vroom')
        #self.assert_link_text_to_url('DJ',     '')
        #self.assert_link_text_to_url('Ticket', '')

        self.fail('TODO : Fix the tests')

    @tests.skipNotFinishedYet
    def test_footer(self):
        '''Test the footer'''
        self.browser.get(self.server_url)

        # You can write to the Mailing List
        self.browser.find_element_by_partial_link_text('bronycub@googlegroups.com')

        # You can see a placeholder message when there is no next humanitarian action

        # You can see the upcoming next humanitarian action

        self.fail('TODO : Write the tests')

    @tests.skipNotFinishedYet
    def test_home_page(self):
        '''Test the home page'''
        # You can see a message when the IRC logs aren't available

        # You can see the IRC logs when available

        # You can see the videos about the brony phenomenon

        # You can see the awesome changing messages under the banner

        self.fail('TODO : Write the tests')

    @tests.skipNotFinishedYet
    def test_agenda(self):
        '''Test the agenda'''

        self.fail('TODO : Write the functionalities and tests')

    @tests.skipNotFinishedYet
    def test_map(self):
        '''Test the map'''
        # You can see the map of the collective's location 

        # You can see the members known location

        # You see the members' avatar if defined else a default avatar

        # Also there's a  button to locate the collective's HQ

        self.fail('TODO : Write the tests')

    @tests.skipNotFinishedYet
    def test_friends(self):
        '''Test the friends map'''
        # You can see the list of friends of this collective

        # You can see the details

        # You can go to their website

        self.fail('TODO : Write the tests')

    @tests.skipNotFinishedYet
    def test_konami(self):
        '''Test that you can trigger the konami easter egg and see the video'''
        # The konami is hidden by default
        self.browser.get(self.server_url)
        try:
            self.browser.find_element_by_id('WhenIm')
        except:
            self.fail('Test is supposed to raise an exception')

        # You can enter the konami code and it triggers an easter egg

        self.browser.find_element_by_id('WhenIm')
        page = self.browser.find_element_by_xpath('//body')
        page.send_keys(Keys.UP)
        page.send_keys(Keys.UP)
        page.send_keys(Keys.DOWN)
        page.send_keys(Keys.DOWN)
        page.send_keys(Keys.LEFT)
        page.send_keys(Keys.RIGHT)
        page.send_keys(Keys.LEFT)
        page.send_keys(Keys.RIGHT)
        page.send_keys('ba')

        # You can now watch a cool video
        self.browser.find_element_by_id('WhenIm')

        self.fail('TODO : Write the tests')

