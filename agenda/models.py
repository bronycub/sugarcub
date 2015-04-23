from django.db                  import models
from django.contrib.auth.models import User

class Event(models.Model):
    ''' Represent an event in the agenda '''

    title       = models.TextField()
    author      = models.OneToOneField(User)
    description = models.TextField()
    date_begin  = models.DateTimeField()
    date_end    = models.DateTimeField()

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    ''' Represent a post in a discussion attached to an event '''

    text   = models.TextField()
    author = models.OneToOneField(User)
    event  = models.OneToOneField(Event)

    def __unicode__(self):
        return self.text
