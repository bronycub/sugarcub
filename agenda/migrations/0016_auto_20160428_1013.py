# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0015_participation_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='participation',
            options={'ordering': ['pseudo']},
        ),
    ]
