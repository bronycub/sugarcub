from   model_mommy                import mommy
from   django.contrib.auth.models import User
from   django.core.urlresolvers   import reverse
from   django.core                import mail
from   django_webtest             import WebTest
from   users.models               import Profile
import datetime
import unittest
import re

class AccountTest(WebTest):

    def setUp(self):
        user = mommy.make(User,
            username   = 'user_test',
            email      = 'email_test',
            first_name = 'first_test',
            last_name  = 'last_test',
        )
        profile = mommy.make(Profile,
            bio      = 'bio_test',
            phone    = '0123456789',
            birthday = datetime.date(1970, 1, 1),
            address  = 'address_test',
            user     = user,
        )
        user.set_password('password_test')
        user.save()

    def test_login(self):
        '''Test that you can login'''
        # You can go to the login page
        page = self.app.get(reverse('auth_login'))

        # You can enter invalid id / password and be warned about it without being logged in
        page.form['username'] = 'user_wrong'
        page.form['password'] = 'password_wrong'
        page = page.form.submit()

        assert reverse('auth_login') in page.request.url
        assert page.html.select('.alert')

        # You can enter correct id / password and be logged in
        page.form['username'] = 'user_test'
        page.form['password'] = 'password_test'
        page = page.form.submit().follow()

        assert reverse('core:home') in page.request.url
        assert 'user_test' in page

    def test_signup(self):
        '''Test that you can create an account'''
        # You can try to register and find yourself in the informations to know before registering page
        page = self.app.get(reverse('users:pre_register'))

        # You can then go to the signup page
        page = page.click(description = "Formulaire d'inscription")

        # You can submit invalid form and be warned about it without creating an account
        page = page.form.submit()
        assert reverse('registration_register') in page.request.url
        assert page.html.select('.has-error')
        assert not mail.outbox

        # You can submit a correct form and create your account
        page.form['registration-username']  = 'user_signup_test'
        page.form['registration-password1'] = 'password_test'
        page.form['registration-password2'] = 'password_test'
        page.form['registration-email']     = 'fluttershy@equestria.pn'
        page.form['user-first_name']        = 'first_test'
        page.form['user-last_name']         = 'last_test'
        page.form['profile-bio']            = 'test'
        page.form['profile-phone']          = '0123456789'
        page.form['profile-birthday']       = '01/01/1970'
        page.form['profile-address']        = 'test'
        page = page.form.submit().follow()

        # You're then redirected to the welcome page and you receive an activation mail
        assert reverse('registration_complete') in page.request.url
        assert mail.outbox

        # You can activate your account
        page = self.app.get(re.search(r'/activate/.*$', mail.outbox[0].body, re.MULTILINE).group()).follow()
        assert reverse('registration_activation_complete') in page.request.url

    def test_login_signup_only_not_logged(self):
        '''Test that the links to the login and signup pages are only present if you\'re not logged'''
        # You can see the login and signup links when you're not logged in
        page = self.app.get(reverse('core:home'))
        assert page.html(href = reverse('auth_login'))
        assert page.html(href = reverse('users:pre_register'))

        # You can't see the login and signup links when you're logged in
        page = self.app.get(reverse('core:home'), user='user_test')
        assert not page.html(href = reverse('auth_login'))
        assert not page.html(href = reverse('users:pre_register'))

    def test_my_account_only_logged(self):
        '''Test that the my account related links are only present when you\'re logged in'''
        # You can't see the my account related links when you're not logged in
        page = self.app.get(reverse('core:home'))
        assert not page.html(href = reverse('users:profile'))

        # You can see the my account related links when you're logged in
        page = self.app.get(reverse('core:home'), user='user_test')
        assert page.html(href = reverse('users:profile'))

    @unittest.skipIf(True, 'not implemented')
    def test_edit_profile(self):
        'Test that you can edit your profile'
        page = self.app.get(reverse('users:profile'), user = 'user_test')

        # Current data are displayed
        assert 'first_test'	  in page
        assert 'last_test'	  in page
        assert 'email_test'	  in page
        assert 'user_test'	  in page
        assert 'bio_test'	  in page
        assert '0123456789'	  in page
        assert '01/01/1970'	  in page
        assert 'address_test' in page

        # You can update your data
        self.fail('TODO : Write the functionalities and tests')

    @unittest.skipIf(True, 'not implemented')
    def test_change_password(self):
        '''Test that you cant change your password'''

        self.fail('TODO : Write the functionalities and tests')

    @unittest.skipIf(True, 'not implemented')
    def test_reset_password(self):
        '''Test that you can reset your password if you forgot it'''

        self.fail('TODO : Write the functionalities and tests')


class MembersTest(WebTest):
    '''Test the functionalitites related to the members page'''

    @unittest.skipIf(True, 'not implemented')
    def test_shows_members(self):
        '''Test that the page shows all (activated) members with their informations'''

        self.fail('TODO : Write the functionalities and tests')

    @unittest.skipIf(True, 'not implemented')
    def test_shows_only_public_not_logged(self):
        '''Test that not logged users can only see informations defined as public'''

        self.fail('TODO : Write the functionalities and tests')

    @unittest.skipIf(True, 'not implemented')
    def test_shows_all_logged(self):
        '''Test that logged users can see all informations'''

        self.fail('TODO : Write the functionalities and tests')

    @unittest.skipIf(True, 'not implemented')
    def test_can_search_list(self):
        '''Test that you can search for particular members by role, skills or hobies'''

        self.fail('TODO : Write the functionalities and tests')

