from django.db					import models
from django.contrib.auth.models import User
from stdimage.models			import StdImageField
from stdimage.utils				import UploadToUUID
from django.core.validators		import RegexValidator

class Profile(models.Model):
    ''' Represent extra data about a User '''

    user			  = models.OneToOneField(User)
    
    bio				  = models.TextField()
    avatar			  = StdImageField(blank = True, null = True,
                            variations = {'avatar': (100, 100), 'small': (50, 50)},
                            upload_to  = UploadToUUID(path = 'avatars'),
                        )
    phone_regex		  = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone			  = models.CharField(validators=[phone_regex], max_length=15)
    birthday		  = models.DateField()
    address			  = models.TextField()
    address_longitude = models.FloatField(blank = True, null = True)
    address_latitude  = models.FloatField(blank = True, null = True)

    def __unicode__(self):
        return self.user.username


class Pony(models.Model):
    ''' List of ponies with little quotes to display in the user's description '''

    profile = models.ForeignKey(Profile)
    pony	= models.CharField(max_length = 32)
    message = models.CharField(max_length = 64)

    def __unicode__(self):
        try:
            return self.message % self.pony
        except TypeError:
            return self.message

    class Meta:
        verbose_name_plural = "ponies"


class Url(models.Model):
    ''' List of urls in the user's description '''

    profile = models.ForeignKey(Profile)
    url		= models.URLField()
    icon	= models.CharField(max_length = 16)

    def __unicode__(self):
        return self.url

