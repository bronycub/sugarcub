from pytest_bdd   import given, when, then, parsers
from urllib.parse import urljoin


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
def i_see_a(browser, text):
    assert browser.is_text_present(text)


@then(parsers.cfparse('I see class {css_class}'))
def i_see_class(browser, css_class):
    assert browser.is_element_present_by_css(css_class)


@then('form has errors')
def form_has_error(browser):
    assert (browser.is_element_present_by_css('.alert-danger') or
            browser.is_element_present_by_css('.has-error'))
