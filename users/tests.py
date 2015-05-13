from   django.test                import TestCase
from   utils                      import tests
from   .                          import views, models, forms
from   django.contrib.auth.views  import login, logout
from   django.contrib.auth.models import User
from   django.core.exceptions     import ValidationError
from   model_mommy                import mommy
import datetime
import unittest

valid_profile_data = {
    'firstname': 'form',
    'lastname':	 'test',
    'bio':		 'test',
    'phone':	 '0123456789',
    'birthday':	 '01/01/1970',
    'address':	 'test',
}

valid_signup_data = {
    'registration-username':  'form_test',
    'registration-password1': 'test',
    'registration-password2': 'test',
    'registration-email':	  'form@test.ts',
    'user-firstname':		  'form',
    'user-lastname':		  'test',
    'profile-bio':			  'test',
    'profile-phone':		  '0123456789',
    'profile-birthday':		  '01/01/1970',
    'profile-address':		  'test',
}


class UsersViewsTest(tests.UnitTestUtilsMixin, TestCase):

    @tests.skipNotFinishedYet
    def test_signup(self):
        self.assert_url_matches_view(views.signup, '/signup', 'registration_register')
        self.fail('todo')

    def test_members(self):
        self.assert_url_matches_view(views.members, '/members', 'users:members')

        profiles = mommy.make(models.Profile, _quantity = 3)
        profiles[0].user.is_active = False
        profiles[0].user.save()

        response = self.client.get('/members')
        self.assertCountEqual(profiles[1:], response.context['profiles'])

    @tests.skipNotFinishedYet
    def test_profile(self):
        self.assert_url_matches_view(views.profile, '/profile', 'users:profile')
        self.fail('todo')


class UsersModelsTest(TestCase):

    def test_name_profile(self):
        user	= mommy.make(models.User,	 username = 'test')
        profile = mommy.make(models.Profile, user	  = user)
        profile.phone = '23456789'
        self.assertRaises(ValidationError, profile.full_clean)

        profile.phone = '0123456789'
        self.assertEquals('test', profile.__unicode__())
        profile.full_clean()

    def test_name_pony(self):
        pony = mommy.make(models.Pony,
            pony	= 'Fluttershy',
            message = '%s is best pony !',
        )
        pony.full_clean()

        self.assertEquals('Fluttershy is best pony !', pony.__unicode__())

        pony = mommy.make(models.Pony,
            pony	= 'Fluttershy',
            message = '%d is best pony !',
        )
        pony.full_clean()

        self.assertEquals('%d is best pony !', pony.__unicode__())

    def test_name_url(self):
        url = mommy.make(models.Url,
            url = 'http://equestria.pn',
        )
        url.full_clean()

        self.assertEquals('http://equestria.pn', url.__unicode__())


class UsersFormsTest(TestCase):

    def test_profile(self):
        form = forms.ProfileForm()
        self.assertFalse(form.is_valid())

        form = forms.ProfileForm(data = valid_profile_data)
        self.assertTrue(form.is_valid())

    def test_signup(self):
        form = forms.RegistrationForm()
        self.assertFalse(form.is_valid())

        form = forms.RegistrationForm(data = valid_signup_data)
        self.assertTrue(form.is_valid())

        models = form.save(user = mommy.make(User))
        self.assertEquals(models['user'], models['profile'].user)
