from   pytest_bdd import scenario
from utils.bdd  import *


@scenario('features/core.feature', 'Access /en/agenda')
@scenario('features/core.feature', 'Access /agenda')
@scenario('features/core.feature', 'Access /en/HQ')
@scenario('features/core.feature', 'Access /HQ')
@scenario('features/core.feature', 'Access /en/map')
@scenario('features/core.feature', 'Access /map')
@scenario('features/core.feature', 'Access /en/friends')
@scenario('features/core.feature', 'Access /friends')
def test_scenario():
    pass
