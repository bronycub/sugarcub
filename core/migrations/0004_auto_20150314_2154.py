# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150129_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='image',
            field=models.ImageField(upload_to='', default=''),
            preserve_default=False,
        ),
    ]
