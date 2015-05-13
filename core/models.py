from django.db import models


class Quote(models.Model):
    ''' List of quotes in the home page '''

    quote = models.TextField()

    def __unicode__(self):
        return self.quote


class Friend(models.Model):
    ''' List of other collectives shown as your friends '''

    name        = models.CharField(max_length = 32)
    description = models.TextField()
    image       = models.ImageField()
    url         = models.URLField()

    def __unicode__(self):
        return self.title


class Event(models.Model):
    ''' List of events the collective has planned '''

    title = models.CharField(max_length = 64)
    host  = models.CharField(max_length = 64)
    link  = models.URLField()
    when  = models.DateTimeField()
    where = models.CharField(max_length = 256)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-when']
