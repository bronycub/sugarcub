from model_mommy                import mommy
from django.contrib.auth.models import User
from django.core.urlresolvers   import reverse
from django_webtest             import WebTest

class AccountTest(WebTest):

	def setUp(self):
		user = mommy.make(User, username='user_test')
		user.set_password('password_test')
		user.save()

	def test_login(self):
		'''Test that you can login'''
		# You can go to the login page
		page = self.app.get(reverse('users:login'))

		# You can enter invalid id / password and be warned about it without being logged in
		page.form['username'] = 'user_wrong'
		page.form['password'] = 'password_wrong'
		page = page.form.submit()

		assert reverse('users:login') in page.request.url 
		assert page.html.select('.alert')

		# You can enter correct id / password and be logged in
		page.form['username'] = 'user_test'
		page.form['password'] = 'password_test'
		page = page.form.submit().follow()

		assert reverse('core:home') in page.request.url 
		assert 'user_test' in page

	def test_signup(self):
		'''Test that you can create an account'''
		# You can go to the signup page
		page = self.app.get(reverse('users:signup'))

		# You can submit invalid form and be warned about it without creating an account
		page = page.form.submit()
		assert reverse('users:signup') in page.request.url 
		assert page.html.select('.has-error')

		# You can submit a correct form and create your account
		page.form['user-username'] = 'user_signup_test'
		page.form['user-password1'] = 'password_test'
		page.form['user-password2'] = 'password_test'
		page.form['profile-bio'] = 'test'
		page.form['profile-gravatar'] = 'test'
		page.form['profile-phone'] = '0123456789'
		page.form['profile-birthday'] = '01/01/1970'
		page.form['profile-address'] = 'test'
		# TODO fill form with valid data
		page = page.form.submit().follow()

		# You're then redirected to the welcome page
		assert reverse('users:signup_success') in page.request.url 

	def test_login_signup_only_not_logged(self):
		'''Test that the links to the login and signup pages are only present if you\'re not logged'''
		# You can see the login and signup links when you're not logged in
		page = self.app.get(reverse('core:home'))
		assert page.html(href = reverse('users:login'))
		assert page.html(href = reverse('users:signup'))

		# You can't see the login and signup links when you're logged in
		page = self.app.get(reverse('core:home'), user='user_test')
		assert not page.html(href = reverse('users:login'))
		assert not page.html(href = reverse('users:signup'))

	def test_my_account_only_logged(self):
		'''Test that the my account related links are only present when you\'re logged in'''
		# You can't see the my account related links when you're not logged in
		page = self.app.get(reverse('core:home'))
		assert not page.html(href = reverse('users:profile'))

		# You can see the my account related links when you're logged in
		page = self.app.get(reverse('core:home'), user='user_test')
		assert page.html(href = reverse('users:profile'))

	def test_edit_profile(self):
		'Test that you can edit your profile'
		self.fail('TODO : Write the functionalities and tests')


class MembersTest(WebTest):
	'''Test the functionalitites related to the members page'''

	def test_shows_members(self):
		'''Test that the page shows all members with their informations'''

		self.fail('TODO : Write the functionalities and tests')

	def test_shows_only_public_not_logged(self):
		'''Test that not logged users can only see informations defined as public'''

		self.fail('TODO : Write the functionalities and tests')

	def test_shows_all_logged(self):
		'''Test that logged users can see all informations'''

		self.fail('TODO : Write the functionalities and tests')

	def test_can_search_list(self):
		'''Test that you can search for particular members by role, skills or hobies'''

		self.fail('TODO : Write the functionalities and tests')

