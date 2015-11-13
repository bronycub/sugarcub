from   pytest_bdd import scenario
from utils.bdd  import *


@scenario('features/core.feature', 'Access /amis')
@scenario('features/core.feature', 'Access /en/friends')
@scenario('features/core.feature', 'Access /fr/amis')
def test_scenario():
    pass
