# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import stdimage.utils
import django.core.validators
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150204_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=stdimage.models.StdImageField(null=True, upload_to=stdimage.utils.UploadToUUID(path='avatars'), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], max_length=15),
            preserve_default=True,
        ),
    ]
