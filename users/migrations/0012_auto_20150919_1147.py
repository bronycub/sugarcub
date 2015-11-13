# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_profile_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='postal_code',
            field=models.CharField(default=33000, max_length=5, validators=[django.core.validators.RegexValidator(message='The postal code must be 5 digits.', regex='^\\d[1-9]\\d{3}$')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(150, message='The bio should be longer than 150 character')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
