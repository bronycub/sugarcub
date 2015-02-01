from django.db                  import models
from django.contrib.auth.models import User

class Profile(models.Model):
	''' Represent extra data about a User '''
	
	bio              = models.TextField()
	gravatar         = models.CharField(blank = True, max_length = 32)
	avatar           = models.ImageField(blank = True, null = True)
	phone            = models.IntegerField()
	birthday         = models.DateField()
	address          = models.TextField()
	addressLongitude = models.FloatField(blank = True, null = True)
	addressLatitude  = models.FloatField(blank = True, null = True)

	user             = models.OneToOneField(User)

	def __unicode__(self):
		return self.user.username

class Pony(models.Model):
	''' List of ponies with little quotes to display in the user's description '''

	profile = models.ForeignKey(Profile)
	pony    = models.CharField(max_length = 32)
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
	url     = models.URLField()
	icon    = models.CharField(max_length = 16)

	def __unicode__(self):
		return self.url

