import sys
from   selenium                           import webdriver
from   selenium.webdriver.common.keys     import Keys
from   django.contrib.staticfiles.testing import StaticLiveServerTestCase

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(self):
        self.browser = webdriver.Firefox()

        for arg in sys.argv:
            if 'liveserver' in arg:
                self.server_url = 'http://' + arg.split('=')[1]
                return

        super().setUpClass()
        self.server_url = self.live_server_url

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

        if self.server_url == self.live_server_url:
            super().tearDownClass()
