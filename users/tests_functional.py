from   pytest_bdd import scenarios, then
from   utils.bdd  import *
import pytest


pytestmark = pytest.mark.django_db
pytestfunctional = pytest.mark.functional


scenarios('features')


@then('I see a form')
def i_see_a_form(browser):
    assert browser.find_by_css('form')


@when('I incorrectly fill the registration form')
def i_incorrectly_fill_registration_form(browser):
    for field in [
        ('registration-username',  'user_signup_test'),
        ('registration-password1', 'password_test'),
        ('registration-password2', 'password_invalid'),
        ('registration-email',     'fluttershy@equestria.pn'),
        ('user-first_name',        'first_test'),
        ('user-last_name',         'last_test'),
        ('profile-bio',            'test'),
        ('profile-phone',          '0123456789'),
        ('profile-birthday',       '01/01/1970'),
        ('profile-address',        'test'),
    ]:
        browser.fill(*field)

    i_submit(browser)


@when('I correctly fill the registration form')
def i_correctly_fill_registration_form(browser):
    for field in [
        ('registration-username',  'user_signup_test'),
        ('registration-password1', 'password_test'),
        ('registration-password2', 'password_test'),
        ('registration-email',     'fluttershy@equestria.pn'),
        ('user-first_name',        'first_test'),
        ('user-last_name',         'last_test'),
        ('profile-bio',            'test'),
        ('profile-phone',          '0123456789'),
        ('profile-birthday',       '01/01/1970'),
        ('profile-address',        'test'),
    ]:
        browser.fill(*field)

    i_submit(browser)


@then('I receive a mail')
def i_receive_a_mail(browser):
    pass
