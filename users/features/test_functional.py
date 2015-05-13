from pytest_bdd import scenario, then
from utils.bdd  import *


@scenario('account.feature', 'See welcome guide and form')
@scenario('account.feature', 'Create account')
def test_publish():
    pass


@then('I see a form')
def i_see_a_form(browser):
    assert browser.find_by_css('form')
