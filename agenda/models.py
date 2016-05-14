from   django.db                  import models
from   django.contrib.auth.models import User
from   django.core.urlresolvers   import reverse
from django.utils.translation     import ugettext_lazy as _
import ics


information_enabled = (
    ('1', _('Show both my phone and my mail')),
    ('2', _('Show only my mail')),
    ('3', _('Show only my phone')),
)


class Event(models.Model):
    ''' Represent an event in the agenda '''

    author        = models.ForeignKey(User, verbose_name = _('user'))

    title         = models.CharField(_('title'), max_length = 500)
    description   = models.TextField(_('description'))
    date_begin    = models.DateTimeField(_('date begin'))
    date_end      = models.DateTimeField(_('date end'))
    address       = models.CharField(_('address'), max_length = 200)
    event_enabled = models.CharField(_('event enabled'), max_length = 10, choices = information_enabled)

    class Meta:
        ordering            = ['-date_begin', '-date_end']
        verbose_name        = _('event')
        verbose_name_plural = _('events')

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

    author = models.ForeignKey(User, verbose_name = _('user'), blank = True, null = True)
    pseudo = models.CharField(_('unregistered user'), max_length = 30, blank = True, null = True)
    event  = models.ForeignKey(Event, verbose_name = _('event'))

    text   = models.TextField(_('text'))
    date   = models.DateTimeField(_('date'), auto_now_add = True)

    class Meta:
        ordering            = ['-date']
        verbose_name        = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return self.text


class Participation(models.Model):
    '''
    Represent a participation to an event by a user

    Participation is made by author if logged in, else by pseudo
    '''

    user    = models.ForeignKey(User, verbose_name = _('user'), null = True, blank = True)
    pseudo  = models.CharField(_('unregistered user'), max_length = 31, blank = True, null=True)
    contact = models.CharField(_('contact'), max_length = 31, blank = True, null = True)
    event   = models.ForeignKey(Event, verbose_name = _('event'))

    class Meta:
        ordering            = ['pseudo']
        verbose_name        = _('participation')
        verbose_name_plural = _('participations')
        unique_together     = (
            ('user', 'event'),
            ('pseudo', 'event'),
        )

    def __str__(self):
        return str(self.author()) + ' ' + str(self.event)

    def author(self):
        return self.user if self.user else self.pseudo
