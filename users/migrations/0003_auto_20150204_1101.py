# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.models
import stdimage.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150203_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=stdimage.models.StdImageField(blank=True, upload_to=stdimage.utils.UploadToUUID(path='avatar'), null=True),
            preserve_default=True,
        ),
    ]
