Feature: Core
	Try all the different Url to access page


Scenario: Access /agenda
	Given I'm on /agenda
	Then I see TODO

Scenario: Access /en/agenda
	Given I'm on /
	When I click on link Agenda
	Then I see TODO

Scenario: Access /HQ
	Given I'm on /HQ
	Then I see Le Quartier Général de BronyCUB !

Scenario: Access /en/HQ
	Given I'm on /
	When I click on link QG
	Then I see Le Quartier Général de BronyCUB !

Scenario: Access /map
	Given I'm on /map
	Then I see Map data

Scenario: Access /en/map
	Given I'm on /
	When I click on link Carte
	Then I see Map data

Scenario: Access /friends
	Given I'm on /friends
	Then I see Aucun ami pour le moment ...

Scenario: Access /en/friends
	Given I'm on /
	When I click on link Nos amis
	Then I see Aucun ami pour le moment ...
