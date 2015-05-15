Feature: Agenda


Scenario: See list of events
	Given I'm on /
	When I click on Agenda
	Then I see a list of events


Scenario: Endless pagination on events
	Given I'm on /agenda
	When I click on 
	Then I see a list of events
