Feature: Account
	Create and Manager your user account


Scenario: See welcome guide
	Given I'm on /
	When I click on link Nous rejoindre ?
	Then I see L'histoire de BronyCUB
	And I see Formulaire d'inscription


Scenario: See registration form
	Given I'm on /
	When I click on link Nous rejoindre ?
	And I click on link Formulaire d'inscription
	Then I see a form


Scenario: Fail to fill registration form
	Given I'm on /register
	When I incorrectly fill the registration form
	Then form has errors


Scenario: Correctly fill registration form and receive confirmation mail
	Given I'm on /register
	When I correctly fill the registration form
	Then I see Bienvenue !
	And I receive a mail


Scenario: No account / Logout buttons when logout
	Given I'm on /
	Then I see Connexion
	And I see Nous rejoindre ?
	Then I don't see Profil
	And I don't see Déconnexion


Scenario: No Login / Signup buttons when logged in
	Given I'm logged in
	And I'm on /
	When I click on user
	Then I see Profil
	And I see Déconnexion
	Then I don't see Connexion
	And I don't see Nous rejoindre ?
