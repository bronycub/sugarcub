# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20150314_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='addressLatitude',
            new_name='address_latitude',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='addressLongitude',
            new_name='address_longitude',
        ),
    ]
