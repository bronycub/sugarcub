from django.db import models


class Quote(models.Model):
    ''' List of quotes in the home page '''

    quote = models.TextField()

    def __str__(self):
        return self.quote


class Friend(models.Model):
    ''' List of other collectives shown as your friends '''

    name        = models.CharField(max_length = 32)
    description = models.TextField()
    image       = models.ImageField()
    url         = models.URLField()

    def __str__(self):
        return self.name
