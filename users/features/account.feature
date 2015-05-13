Feature: Account
	Create and Manager your user account

Scenario: See welcome guide and form
	Given I'm on /
	When I click on Nous rejoindre ?
	Then I see L'histoire de BronyCUB
	And I see Formulaire d'inscription

Scenario: Create account
	Given I'm on /
	When I click on Nous rejoindre ?
	And I click on Formulaire d'inscription
	Then I see a form
