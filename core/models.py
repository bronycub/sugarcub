from django.db                  import models
from django.contrib.auth.models import User

class Profile(models.Model):
	''' Represent extra data about a User '''
	
	bio               = models.TextField()
	gravatar          = models.CharField(max_length = 32)
	phone             = models.IntegerField()
	birthday          = models.DateField()
	address           = models.TextField()
	addressLongitude  = models.FloatField()
	addressLontatidue = models.FloatField()

	user              = models.OneToOneField(User)

	def __unicode__(self):
		return user.username

class Pony(models.Model):
	''' List of ponies with little quotes to display in the user's description '''

	user    = models.ForeignKey(User)
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

class Quote(models.Model):
	''' List of quotes in the home page '''

	quote = models.TextField()

	def __unicode__(self):
		return self.quote

class Friend(models.Model):
	''' List of other associations shown as your friends '''

	name        = models.CharField(max_length = 32)
	description = models.TextField()
	url         = models.URLField()

	def __unicode__(self):
		return self.title

class Event(models.Model):
	''' List of events the association has planned '''

	title = models.CharField(max_length = 64)
	host  = models.CharField(max_length = 64)
	link  = models.URLField()
	when  = models.DateTimeField()
	where = models.CharField(max_length = 256)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-when']
