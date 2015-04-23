from django.db                  import models
from django.contrib.auth.models import User

class Event(models.Model):
    ''' Represent an event in the agenda '''

    author      = models.ForeignKey(User)

    title       = models.TextField()
    description = models.TextField()
    date_begin  = models.DateTimeField()
    date_end    = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_begin', '-date_end']

class Comment(models.Model):
    '''
    Represent a post in a discussion attached to an event

    Comment is posted by author if logged in, else by pseudo
    '''

    author = models.ForeignKey(User, null = True)
    pseudo = models.CharField(max_length = 30, blank = True)
    event  = models.ForeignKey(Event)

    text   = models.TextField()
    date   = models.DateTimeField()

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-date']

class Participation(models.Model):
    '''
    Represent a participation to an event by a user

    Participation is made by author if logged in, else by pseudo
    '''

    user   = models.ForeignKey(User, null = True)
    pseudo = models.CharField(max_length = 31, blank = True)
    event  = models.OneToOneField(Event)

    def __str__(self):
        return (str(self.user) if self.user else self.pseudo) + ' ' + str(self.event)
