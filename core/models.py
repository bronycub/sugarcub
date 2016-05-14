from django.db                import models
from django.utils.translation import ugettext_lazy as _


class Quote(models.Model):
    ''' List of quotes in the home page '''

    quote = models.TextField(_('quote'))

    class Meta:
        verbose_name        = _('quote')
        verbose_name_plural = _('quotes')

    def __str__(self):
        return self.quote


class Friend(models.Model):
    ''' List of other collectives shown as your friends '''

    name        = models.CharField(_('name'), max_length = 32)
    description = models.TextField(_('description'))
    image       = models.ImageField(_('image'))
    url         = models.URLField(_('url'))

    class Meta:
        verbose_name        = _('friend')
        verbose_name_plural = _('friends')

    def __str__(self):
        return self.name
