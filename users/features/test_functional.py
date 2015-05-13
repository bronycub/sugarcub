from pytest_bdd import scenario, given, when, then, parsers


@scenario('account.feature', 'See welcome guide and form')
@scenario('account.feature', 'Create account')
def test_publish():
    pass


@given("I am on /")
@given("I'm on /")
def i_am_on(browser):
    browser.visit('localhost:8000/')


@when(parsers.cfparse('I click on {link}'))
def i_click_on(browser, link):
    browser.find_link_by_partial_text(link)[0].click()


@then(parsers.cfparse('I see {text}'))
def i_see_a(browser, text):
    assert browser.is_text_present(text)


@then('I see a form')
def i_see_a_form(browser):
    assert browser.find_by_css('form')
