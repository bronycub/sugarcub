from   pytest_bdd  import scenario
from   utils.bdd   import *
from   model_mommy import mommy
from   .           import models


@scenario('features/agenda.feature', 'See a list of events')
@scenario('features/agenda.feature', 'See a list of comments')
@scenario('features/agenda.feature', 'Endless pagination on events')
@scenario('features/agenda.feature', 'Endless pagination on comments')
@scenario('features/agenda.feature', "Don't see comments when not logged in")
def test_feature(live_server):
    pass


@given('I have events')
def events():
    events = mommy.make(models.Event, _quantity = 50)
    return events


@given('I have comments')
def comments(events):
    comments = []
    for event in events:
        comments.extend(mommy.make(models.Comment, _quantity = 20, event = event))

    return comments


@when('I click on an event')
def i_click_event(browser):
    browser.find_by_css('.event a').first.click()


@then(parsers.cfparse('I see a list of {count:integer} events', extra_types=dict(integer=int)))
def i_see_events(browser, count):
    assert count == len(browser.find_by_css('.event'))


@then("I don't see any events")
def i_see_no_events(browser, count):
    i_see_events(browser, 0)


@then(parsers.cfparse('I see a list of {count:integer} comments', extra_types=dict(integer=int)))
def i_see_comments(browser, count):
    assert count == len(browser.find_by_css('.event .in .comment'))


@then("I don't see any comments")
def i_see_no_comments(browser, count):
    i_see_comments(browser, 0)
