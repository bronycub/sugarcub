# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0008_event_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_enabled',
            field=models.CharField(default=1, choices=[(1, 'Show both my phone and my mail to contacted by people'), (2, 'Show only my mail to contacted by people'), (3, 'Show only my phone contacted by people')], max_length=1),
            preserve_default=False,
        ),
    ]
