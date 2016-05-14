from pytest_bdd import scenario
from utils.bdd  import *


@scenario('features/agenda.feature', 'Todo')
def test_feature(live_server):
    pass
