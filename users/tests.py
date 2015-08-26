from   django.test                import TestCase
from   .                          import models, forms
from   django.contrib.auth.models import User
from   django.core.exceptions     import ValidationError
from   model_mommy                import mommy
import pytest


pytestmark = pytest.mark.logical


valid_profile_data = {
    'firstname': 'form',
    'lastname':  'test',
    'bio':       'test',
    'phone':     '0123456789',
    'birthday':  '01/01/1970',
    'address':   'test',
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
}


class UsersModelsTest(TestCase):

    def test_name_profile(self):
        user    = mommy.make(models.User,    username = 'test')
        profile = mommy.make(models.Profile, user     = user)
        profile.phone = '23456789'
        with pytest.raises(ValidationError):
            profile.full_clean()

        profile.phone = '0123456789'
        assert 'test' == profile.__unicode__()
        profile.full_clean()

    def test_name_pony(self):
        pony = mommy.make(models.Pony,
            pony    = 'Fluttershy',
            message = '%s is best pony !',
        )
        pony.full_clean()

        assert 'Fluttershy is best pony !' == pony.__unicode__()

        pony = mommy.make(models.Pony,
            pony    = 'Fluttershy',
            message = '%d is best pony !',
        )
        pony.full_clean()

        assert '%d is best pony !' == pony.__unicode__()

    def test_name_url(self):
        url = mommy.make(models.Url,
            url = 'http://equestria.pn',
        )
        url.full_clean()

        assert 'http://equestria.pn' == url.__unicode__()

    def test_get_active_users(self):
        profiles = mommy.make(models.Profile, _quantity = 3)

        # Test avec enabled = False et is_active = True
        self.assertCountEqual(profiles[:0], models.Profile.objects.get_active_users())

        # Test avec enabled = True et is_active = True
        profiles[0].enabled = True
        profiles[0].save()
        profiles[1].enabled = True
        profiles[1].save()
        self.assertCountEqual(profiles[:2], models.Profile.objects.get_active_users())

        # Test avec enabled = True et is_active = False
        profiles[0].user.is_active = False
        profiles[0].user.save()
        profiles[1].user.is_active = False
        profiles[1].user.save()
        self.assertCountEqual(profiles[:0], models.Profile.objects.get_active_users())

        # Test avec enabled = False et is_active = False
        profiles[0].enabled = False
        profiles[0].save()
        profiles[1].enabled = False
        profiles[1].save()
        self.assertCountEqual(profiles[:0], models.Profile.objects.get_active_users())


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
