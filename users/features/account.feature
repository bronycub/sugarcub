Feature: Account
	Create and Manager your user account


Scenario: Login
	Given I have a user account
	When I log in
	Then I see Fluttershy


Scenario: See welcome guide
	Given I'm not logged in
	Given I'm on /
	When I click on link Nous rejoindre ?
	Then I see L'histoire de BronyCUB
	Then I see Formulaire d'inscription


Scenario: See registration form
	Given I'm not logged in
	Given I'm on /
	When I click on link Nous rejoindre ?
	When I click on link Formulaire d'inscription
	Then I see a form


Scenario: Fail to fill registration form
	Given I'm not logged in
	Given I'm on /register
	When I incorrectly fill the registration form
	Then form has errors


Scenario: Correctly fill registration form and receive confirmation mail
	Given I'm not logged in
	Given I'm on /register
	When I correctly fill the registration form
	Then I see Bienvenue !
	Then I receive a mail


Scenario: No account / Logout buttons when logout
	Given I'm not logged in
	Given I'm on /
	Then I see Connexion
	Then I see Nous rejoindre ?
	Then I don't see Profil
	Then I don't see Déconnexion


Scenario: No Login / Signup buttons when logged in
	Given I'm logged in
	Given I'm on /
	When I click on link Fluttershy
	Then I see Profil
	Then I see Déconnexion
	Then I don't see Connexion
	Then I don't see Nous rejoindre ?


Scenario: See Profil form
	Given I'm logged in
	Given I'm on /
	When I click on link Profil
	Then I see a form


Scenario: Change profile value
	Given I'm logged in
	Given I'm on /profile
	When I correctly fill the profile form
	Then I see profile_address
	Then I see profile_bio

