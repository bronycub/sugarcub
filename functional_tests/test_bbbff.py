from   functional_tests.base import FunctionalTest
from   utils                 import tests
import pytest


@pytest.mark.functional
class BbbffTest(FunctionalTest):
    '''Test BBBFF functionalitites'''

    @tests.skipNotFinishedYet
    def test_todo(self):
        self.fail('TODO : Write the functional tests')
