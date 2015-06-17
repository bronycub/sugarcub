import pytest


skipNotFinishedYet = pytest.mark.skipif(True, reason = 'not implemented')


pytestmark = pytest.mark.logical
