from   pytest_bdd import scenario, then
from   utils.bdd  import *


@scenario('features/account.feature', 'Login')
@scenario('features/account.feature', 'See welcome guide')
@scenario('features/account.feature', 'See registration form')
@scenario('features/account.feature', 'Fail to fill registration form')
@scenario('features/account.feature', 'Correctly fill registration form and receive confirmation mail')
@scenario('features/account.feature', 'No account / Logout buttons when logout')
@scenario('features/account.feature', 'No Login / Signup buttons when logged in')
def test_feature(live_server):
    pass


registration_form_data = {
    'registration-username':  'user_signup_test',
    'registration-password1': 'password_test',
    'registration-email':     'fluttershy@equestria.pn',
    'user-first_name':        'first_test',
    'user-last_name':         'last_test',
    'profile-bio':            'test',
    'profile-phone':          '0123456789',
    'profile-birthday':       '01/01/1970',
    'profile-address':        'test',
}


def fill_registration_form(password2, browser):
    registration_form_data['registration-password2'] = password2
    for field in registration_form_data.items():
        browser.fill(*field)

    i_submit(browser)


@then('I see a form')
def i_see_a_form(browser):
    assert browser.find_by_css('form')


@when('I incorrectly fill the registration form')
def i_incorrectly_fill_registration_form(browser):
    fill_registration_form('password_invalid', browser)


@when('I correctly fill the registration form')
def i_correctly_fill_registration_form(browser):
    fill_registration_form('password_test', browser)


@then('I receive a mail')
def i_receive_a_mail(browser):
    pass
