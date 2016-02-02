# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0012_auto_20160202_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='pseudo',
            field=models.CharField(max_length=31, blank=True, null=True),
        ),
    ]
