# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150314_2154'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
    ]
