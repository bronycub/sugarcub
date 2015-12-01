Feature: Core
	Try all the different Url to access page


Scenario: Access /amis
	When I am on '/amis'
	Then I see 'Aucun ami pour le moment ...'

Scenario: Access /en/friends
	When I am on '/en/friends'
	Then I see 'Aucun ami pour le moment ...'

Scenario: Access /fr/amis
	When I am on '/'
	When I click on link 'Nos amis'
	Then I see 'Aucun ami pour le moment ...'
