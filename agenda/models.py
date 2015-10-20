from   django.db                  import models
from   django.contrib.auth.models import User
from   django.core.urlresolvers   import reverse
import ics


class Event(models.Model):
    ''' Represent an event in the agenda '''

    author      = models.ForeignKey(User)

    title       = models.TextField()
    description = models.TextField()
    date_begin  = models.DateTimeField()
    date_end    = models.DateTimeField()
    event_phone_enabled = models.BooleanField(default = False)
    event_mail_enabled = models.BooleanField(default = False)
    address     = models.CharField(max_length = 200)

    class Meta:
        ordering = ['-date_begin', '-date_end']

    def get_absolute_url(self):
        return reverse('event', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def __init__(self, *args, ics_import = None, **kwargs):
        super().__init__(*args, **kwargs)
        if ics_import is not None:
            self.from_ics_event(ics_import)

    def from_ics_event(self, ics_event):
        self.title       = ics_event.name
        self.date_begin  = ics_event.begin.naive
        self.date_end    = ics_event.end.naive
        self.description = ics_event.description

    def to_ics_event(self):
        return ics.Event(
            name        = self.title,
            begin       = self.date_begin,
            end         = self.date_end,
            description = self.description,
        )


class Comment(models.Model):
    '''
    Represent a post in a discussion attached to an event

    Comment is posted by author if logged in, else by pseudo
    '''

    author = models.ForeignKey(User, blank = True, null = True)
    pseudo = models.CharField(max_length = 30, blank = True, null = True)
    event  = models.ForeignKey(Event)

    text   = models.TextField()
    date   = models.DateTimeField(auto_now_add = True)

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
        return str(self.author()) + ' ' + str(self.event)

    def author(self):
        return self.user if self.user else self.pseudo
