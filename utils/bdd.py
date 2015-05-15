from   pytest_bdd                 import given, when, then, parsers
from   urllib.parse               import urljoin
from   django.contrib.auth.models import User
from   model_mommy                import mommy
import pytest


pytestmark = [pytest.mark.django_db, pytest.mark.functional]


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


@when('I log out')
def i_log_out(browser):
    i_click_on_link(browser, 'Déconnexion')


@when('I log in')
def i_log_in(browser, live_server, user_account):
    i_am_on(browser, '/', live_server)
    i_click_on_link(browser, 'Connexion')
    browser.fill('username', user_account.username)
    browser.fill('password', 'password_test')
    i_submit(browser)


@given(parsers.cfparse('I am on {url}'))
@given(parsers.cfparse("I'm on {url}"))
def i_am_on(browser, url, live_server):
    browser.visit(urljoin(live_server.url, url))


@when(parsers.cfparse('I click on link {link}'))
def i_click_on_link(browser, link):
    browser.click_link_by_partial_text(link)


@when(parsers.cfparse('I submit'))
def i_submit(browser):
    browser.find_by_css('button[type=submit]').first.click()


@then(parsers.cfparse('I see {text}'))
def i_see(browser, text):
    assert browser.is_text_present(text)


@then(parsers.cfparse("I don't see {text}"))
def i_dont_see(browser, text):
    assert not browser.is_text_present(text)


@then(parsers.cfparse('I see class {css_class}'))
def i_see_class(browser, css_class):
    assert browser.is_element_present_by_css(css_class)


@then('form has errors')
def form_has_error(browser):
    assert (browser.is_element_present_by_css('.alert-danger') or
            browser.is_element_present_by_css('.has-error'))
