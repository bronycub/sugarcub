# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='friend',
            options={'verbose_name_plural': 'friends', 'verbose_name': 'friend'},
        ),
        migrations.AlterModelOptions(
            name='quote',
            options={'verbose_name_plural': 'quotes', 'verbose_name': 'quote'},
        ),
        migrations.AlterField(
            model_name='friend',
            name='description',
            field=models.TextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='name',
            field=models.CharField(verbose_name='name', max_length=32),
        ),
        migrations.AlterField(
            model_name='friend',
            name='url',
            field=models.URLField(verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.TextField(verbose_name='quote'),
        ),
    ]
