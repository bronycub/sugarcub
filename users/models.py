from   django.db                  import models
from   django.contrib.auth.models import User
from   stdimage.models            import StdImageField
from   stdimage.utils             import UploadToUUID
from   django.core.validators     import RegexValidator, MinLengthValidator
from   django.utils.translation   import ugettext_lazy as _
from   datetime                   import date, timedelta
from   contextlib                 import suppress
from   celery                     import shared_task
from   .                          import fields, validators
import requests


class UrlField(models.CharField):
    default_validators = [validators.UrlValidator()]

    def __init__(self, verbose_name=None, name=None, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 200)
        super().__init__(**kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': fields.UrlField,
        }
        defaults.update(kwargs)
        return super(UrlField, self).formfield(**defaults)


class ProfileManager(models.Manager):
    ''' Manager of the Profile model '''

    def get_active_users(self):
        '''
        Return a QuerySet of all profiles of active users
        ie profile.enabled == True and user.is_active == True
        '''

        return self.model.objects.filter(enabled = True, user__is_active = True)

    def get_birthday(self):
        ''' Return all profile with birthday today '''

        return self.model.objects.filter(birthday__day = date.today().day, birthday__month = date.today().month,
            enabled = True, user__is_active = True, birthday_enabled = True)

    def get_new_members(self):
        ''' Return profile registered within the last 30 days '''

        return self.model.objects.filter(
            user__date_joined__range=(date.today() - timedelta(days=30), date.today()),
            enabled = True, user__is_active = True)


class Profile(models.Model):
    ''' Represent extra data about a User '''

    objects           = ProfileManager()
    phone_regex       = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_(
        "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    zipcode_regex     = RegexValidator(regex=r'^\d[1-9]\d{3}$', message=_(
        "The postal code must be 5 digits."))

    user              = models.OneToOneField(User, verbose_name = _('user'))

    enabled           = models.BooleanField(_('enabled'), default = False)
    name_enabled      = models.BooleanField(_('name enabled'), default = True)
    mail_enabled      = models.BooleanField(_('mail enabled'), default = True)

    bio_min_size      = MinLengthValidator(150, message=_(
        'The bio should be longer than 150 character'))
    bio               = models.TextField(_('bio'), validators=[bio_min_size])
    avatar            = StdImageField(_('avatar'), blank = True, null = True,
        variations = {'avatar': (100, 100), 'small': (50, 50), 'big': (222, 222)},
        upload_to  = UploadToUUID(path = 'avatars'),
    )

    phone             = models.CharField(_('phone'), validators=[phone_regex], max_length=15)
    phone_enabled     = models.BooleanField(_('phone enabled'), default = True)

    birthday          = models.DateField(_('birthday'))
    birthday_enabled  = models.BooleanField(_('birthday enabled'), default = True)

    address           = models.CharField(_('address'), max_length=200)
    city              = models.CharField(_('city'), max_length=30)
    postal_code       = models.CharField(_('postal code'), max_length=5, validators=[zipcode_regex])
    address_enabled   = models.BooleanField(_('address enabled'), default = True)

    address_longitude = models.FloatField(_('longitude'), blank = True, null = True)
    address_latitude  = models.FloatField(_('latitude'), blank = True, null = True)

    class Meta:
        verbose_name        = _('profile')
        verbose_name_plural = _('profiles')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        get_gps_position.delay(self.id)


@shared_task
def get_gps_position(profile_id):
    ''' Update latitude and longitude form address using nominatim api '''

    profile = Profile.objects.get(pk = profile_id)

    with suppress(Exception):
        doc = requests.get(
            'https://nominatim.openstreetmap.org/search',
            {'q': profile.address + ' ' + profile.city, 'format': 'json'}
        ).json()

        profile.address_latitude = float(doc[0]['lat'])
        profile.address_longitude = float(doc[0]['lon'])


class Pony(models.Model):
    ''' List of different pony available '''

    name      = models.CharField(_('name'), max_length = 32)
    file_name = models.CharField(_('file name'), max_length = 32)

    class Meta:
        verbose_name        = _('pony icon')
        verbose_name_plural = _('pony icons')

    def __str__(self):
        return self.name


class Icon(models.Model):
    ''' List of different icon available '''

    name      = models.CharField(_('name'), max_length = 32)

    class Meta:
        verbose_name        = _('site icon')
        verbose_name_plural = _('site icons')

    def __str__(self):
        return self.name


class UserPony(models.Model):
    ''' List of ponies with little quotes to display in the user's description '''

    profile = models.ForeignKey(Profile, verbose_name = _('profile'))
    pony    = models.ForeignKey(Pony, verbose_name = _('pony'))
    message = models.CharField(_('message'), max_length = 64)

    class Meta:
        verbose_name        = _('pony')
        verbose_name_plural = _('ponies')

    def __str__(self):
        try:
            return self.message % self.pony
        except TypeError:
            return self.message


class UserUrl(models.Model):
    ''' List of urls in the user's description '''

    profile = models.ForeignKey(Profile, verbose_name = _('profil'))
    url     = UrlField(_('url'))
    icon    = models.ForeignKey(Icon, verbose_name = _('icon'))

    class Meta:
        verbose_name        = _('url')
        verbose_name_plural = _('urls')

    def __str__(self):
        return self.url
