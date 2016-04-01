from   pytest_bdd                 import given, when, then, parsers
from   urllib.parse               import urljoin
from   django.contrib.auth.models import User
from   model_mommy                import mommy
from   time                       import sleep
import pytest
import random


pytestmark = pytest.mark.django_db


@given('I have a user account')
def user_account():
    user = mommy.make(User, username = 'Fluttershy')
    user.set_password('password_test')
    user.save()
    return user


@given('I am not logged in')
@given("I'm not logged in")
def i_m_not_logged_in(browser):
    browser.cookies.delete()


@given('I am logged in')
@given("I'm logged in")
def i_m_logged_in(browser, live_server, user_account):
    i_log_in(browser, live_server, user_account)
    return user_account


@when('I log in')
def i_log_in(browser, live_server, user_account):
    i_am_on(browser, '/', live_server)
    i_click_on_link(browser, 'Connexion')
    browser.fill('username', user_account.username)
    browser.fill('password', 'password_test')
    i_submit(browser)


@when(parsers.cfparse("I am on '{url}'"))
@when(parsers.cfparse("I'm on '{url}'"))
def i_am_on(browser, url, live_server):
    browser.visit(urljoin(live_server.url, url))


@when(parsers.cfparse("I click on link '{link}'"))
def i_click_on_link(browser, link):
    browser.click_link_by_partial_text(link)


@when(parsers.cfparse('I submit'))
def i_submit(browser):
    random.choice(
        browser.find_by_css('button[type=submit]')
    ).click()


@when('I wait')
def i_wait():
    sleep(5)


@when(parsers.cfparse('I fill {element} with {content}'))
def fill_in_form(browser, element, content):
    browser.fill(element, content)


@then(parsers.cfparse("I see '{text}'"))
def i_see(browser, text):
    assert browser.is_text_present(text)


@then(parsers.cfparse("I don't see '{text}'"))
def i_dont_see(browser, text):
    assert not browser.is_text_present(text)


@given(parsers.cfparse("Todo"))
def given_todo():
    pass


@when(parsers.cfparse("Todo"))
def when_todo():
    pass


@then(parsers.cfparse("Todo"))
def then_todo():
    assert True


@then('form has errors')
def form_has_error(browser):
    assert (browser.is_element_present_by_css('.alert-danger') or
            browser.is_element_present_by_css('.has-error'))
