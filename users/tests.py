from   django.test                import TestCase
from   .                          import models, forms, test_data
from   django.contrib.auth.models import User
from   django.core.exceptions     import ValidationError
from   model_mommy                import mommy
import pytest


valid_profile_data = {
    'firstname':   'form',
    'lastname':    'test',
    'bio':         'test',
    'phone':       '0123456789',
    'birthday':    '01/01/1970',
    'address':     'test',
    'city':        'test',
    'postal_code': '33000',
}


valid_signup_data = {
    'registration-username':  'form_test',
    'registration-password1': 'test',
    'registration-password2': 'test',
    'registration-email':     'form@test.ts',
    'user-firstname':         'form',
    'user-lastname':          'test',
    'profile-bio':            'test',
    'profile-phone':          '0123456789',
    'profile-birthday':       '01/01/1970',
    'profile-address':        'test',
    'profile-city':           'test',
    'profile-postal_code':    '33000',
}


class UsersModelsTest(TestCase):

    def test_name_profile(self):
        user    = mommy.make(models.User,    username = 'test')
        profile = mommy.make(models.Profile, user     = user)

        profile.postal_code = '00000'
        profile.phone = '0123456789'
        with pytest.raises(ValidationError):
            profile.full_clean()

        profile.postal_code = '33000'
        profile.phone = '23456789'
        with pytest.raises(ValidationError):
            profile.full_clean()

        profile.postal_code = '33000'
        profile.phone = '0123456789'
        assert 'test' == profile.__str__()
        profile.full_clean()

    def test_name_pony(self):
        pony = mommy.make(models.UserPony,
            pony    = 'Fluttershy',
            message = '%s is best pony !',
        )
        pony.full_clean()

        assert 'Fluttershy is best pony !' == pony.__str__()

        pony = mommy.make(models.UserPony,
            pony    = 'Fluttershy',
            message = '%d is best pony !',
        )
        pony.full_clean()

        assert '%d is best pony !' == pony.__str__()

    def test_name_url(self):
        url = mommy.make(models.UserUrl,
            url = 'http://equestria.pn',
        )
        url.full_clean()

        assert 'http://equestria.pn' == url.__str__()

    def test_get_active_users(self):
        profiles = test_data.create_profiles()

        self.assertCountEqual(profiles[3:], models.Profile.objects.get_active_users())


class UsersFormsTest(TestCase):

    def test_profile(self):
        form = forms.ProfileForm()
        assert not form.is_valid()

        form = forms.ProfileForm(data = valid_profile_data)
        assert form.is_valid()

    def test_signup(self):
        form = forms.RegistrationForm()
        assert not form.is_valid()

        form = forms.RegistrationForm(data = valid_signup_data)
        assert form.is_valid()

        models = form.save(user = mommy.make(User))
        assert  models['user'] == models['profile'].user
