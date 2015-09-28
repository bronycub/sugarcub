Feature: Agenda
	Agenda features: list events, list comments, create events, post comments, export agenda


	Background:
		Given I have events
		Given I have comments


	Scenario: See a list of events
		Given I'm logged in
		When I'm on '/'
		When I click on link 'Agenda'
		Then I see a list of 10 events
		Then I don't see any comments


	Scenario: See a list of comments
		Given I'm logged in
		When I'm on '/agenda'
		When I click on an event
		Then I see a list of 10 events
		Then I see a list of 3 comments


	Scenario: Endless pagination on events
		Given I'm logged in
		When I'm on '/agenda'
		When I click on an event
		When I click on link 'more events'
		When I wait
		Then I see a list of 20 events
		Then I see a list of 3 comments


	Scenario: Endless pagination on comments
		Given I'm logged in
		When I'm on '/agenda'
		When I click on an event
		When I click on link 'more comments'
		When I wait
		Then I see a list of 10 events
		Then I see a list of 13 comments


	Scenario: Don't see comments when not logged in
		Given I'm not logged in
		When I'm on '/agenda'
		When I click on an event
		Then I see a list of 10 events
		Then I don't see any comments
		Then I see 'You must be logged in to see the comments.'


	Scenario: Export events
		Given I'm not logged in
		When I'm on '/agenda'
		When I click on link 'Download the caldendar'
		Then the downloaded file is a valid ics


#	Scenario: Participate to an event


#	Scenario: Unparticipate to an event


#	Scenario: Add event


	Scenario: Post comment logged in
		Given I'm logged in
		When I'm on '/agenda'
		When I click on an event
		When I fill .post-comment input with Count me in ;)
		When I press 'Enter'
		Then '.post-comment input' is empty
		Then the first comment is 'Count me in ;)


	Scenario: Comment posted is still present
		Given I'm logged in
		When I'm on '/agenda'
		When I click on an event
		Then '.post-comment input' is empty
		Then the first comment is 'Count me in ;)
