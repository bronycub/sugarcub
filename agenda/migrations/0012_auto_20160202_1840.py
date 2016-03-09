# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0011_auto_20151102_1650'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together=set([('user', 'event'), ('pseudo', 'event')]),
        ),
    ]
