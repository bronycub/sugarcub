from   pytest_bdd  import scenario, then
from   .           import models
from   model_mommy import mommy
from   utils.bdd   import *


@scenario('features/account.feature', 'Login')
@scenario('features/account.feature', 'Logout')
@scenario('features/account.feature', 'See welcome guide')
@scenario('features/account.feature', 'See registration form')
@scenario('features/account.feature', 'Fail to fill registration form')
@scenario('features/account.feature', 'Correctly fill registration form and receive confirmation mail')
@scenario('features/account.feature', 'No account / Logout buttons when logout')
@scenario('features/account.feature', 'No Login / Signup buttons when logged in')
@scenario('features/account.feature', 'See Profil form')
@scenario('features/account.feature', 'Change profile value')
@scenario('features/account.feature', 'Change in profile stay')
@scenario('features/account.feature', 'I see change password')
# @scenario('features/account.feature', 'Failed to fill the change password form')
# @scenario('features/account.feature', 'Succeed to fill the change password form')
@scenario('features/account.feature', 'I can see members')
@scenario('features/account.feature', 'I can see members profile')
@scenario('features/account.feature', "I can't see members profile")
def test_feature(live_server):
    pass


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


@when('I correctly fill the profile form')
def i_correctly_fill_profile_form(browser):
    for field in [
        ('bio',         'profile_bio'),
        ('phone',       '0123456789'),
        ('address',     'profile_address'),
        ('birthday',    '01/01/2015'),
    ]:
        browser.fill(*field)

    i_submit(browser)


@when('I incorrectly fill the password form')
def i_incorrectly_fill_the_password_form(browser):
    for field in [
        ('old_password',        'error_password_test'),
        ('new_password1',       'new_password_test'),
        ('new_password2',       'new_password_test'),
    ]:
        browser.fill(*field)

    i_submit(browser)


@when('I correctly fill the password form')
def i_correctly_fill_the_password_form(browser):
    for field in [
        ('old_password',        'password_test'),
        ('new_password1',       'new_password_test'),
        ('new_password2',       'new_password_test'),
    ]:
        browser.fill(*field)

    i_submit(browser)


@then('I receive a mail')
def i_receive_a_mail(browser):
    pass

@given('There is active members')
def there_is_active_members(browser):
    profile = mommy.make(models.Profile)
    profile.user.username = "Fluttershy_profile"
    profile.user.save()
    profile.bio = "profile_bio"
    profile.enabled = True
    profile.save()