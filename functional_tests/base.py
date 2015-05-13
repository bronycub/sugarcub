import sys
import os
from   selenium                           import webdriver
from   django.contrib.staticfiles.testing import StaticLiveServerTestCase
from   datetime                           import datetime


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

    def run(self, result=None):
        override = ScreenshotTaker(result, self.browser)
        super().run(result)
        override.release()


class ScreenshotTaker:

    def __init__(self, result, webdriver):
        self._result = result
        self._webdriver = webdriver

        if self._result is not None:
            self._old_addFailure           = result.addFailure
            self._old_addError             = result.addError
            self._old_addUnexpectedSuccess = result.addUnexpectedSuccess

            self._result.addFailure           = self.addFailure
            self._result.addError             = self.addError
            self._result.addUnexpectedSuccess = self.addUnexpectedSuccess

    def release(self):
        if self._result is not None:
            self._result.addFailure           = self._old_addFailure
            self._result.addError             = self._old_addError
            self._result.addUnexpectedSuccess = self._old_addUnexpectedSuccess

    def addFailure(self, test, err):
        self._take_screenshot(test)
        if self._result is not None:
            self._old_addFailure(test, err)

    def addError(self, test, err):
        self._take_screenshot(test)
        if self._result is not None:
            self._old_addError(test, err)

    def addUnexpectedSuccess(self, test):
        self._take_screenshot(test)
        if self._result is not None:
            self._old_addUnexpectedSuccess(test)

    def _take_screenshot(self, test):
        filename = os.getenv('SELENIUM_SCREENSHOTS_PATH', '')
        if filename == '':
            return

        filename = os.path.join(filename, self._test_start_time.__str__())
        os.makedirs(filename, exist_ok=True)
        filename = os.path.join(filename, test.__str__() + '.png')

        try:
            self._webdriver.save_screenshot(filename)
        except:
            print('Failed to save the screenshot: ' + filename)

    _test_start_time = datetime.now()
