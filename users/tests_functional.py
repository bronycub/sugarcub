from pytest_bdd import scenario
from utils.bdd  import *


@scenario('features/account.feature', 'Todo')
def test_feature(live_server):
    pass
