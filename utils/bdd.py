from pytest_bdd   import given, when, then, parsers
from urllib.parse import urljoin


@given(parsers.cfparse("I am on {url}"))
@given(parsers.cfparse("I'm on {url}"))
def i_am_on(browser, url):
    browser.visit(urljoin('http://localhost:8000/', url))


@when(parsers.cfparse('I click on {link}'))
def i_click_on(browser, link):
    browser.find_link_by_partial_text(link)[0].click()


@then(parsers.cfparse('I see {text}'))
def i_see_a(browser, text):
    assert browser.is_text_present(text)
