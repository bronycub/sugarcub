# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import stdimage.models
from django.conf import settings
import stdimage.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icon',
            options={'verbose_name_plural': 'icons', 'verbose_name': 'icon'},
        ),
        migrations.AlterModelOptions(
            name='pony',
            options={'verbose_name_plural': 'ponies', 'verbose_name': 'pony'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'profiles', 'verbose_name': 'profile'},
        ),
        migrations.AlterModelOptions(
            name='userpony',
            options={'verbose_name_plural': 'ponies', 'verbose_name': 'pony'},
        ),
        migrations.AlterModelOptions(
            name='userurl',
            options={'verbose_name_plural': 'urls', 'verbose_name': 'url'},
        ),
        migrations.AlterField(
            model_name='icon',
            name='file_name',
            field=models.CharField(verbose_name='file name', max_length=32),
        ),
        migrations.AlterField(
            model_name='icon',
            name='name',
            field=models.CharField(verbose_name='name', max_length=32),
        ),
        migrations.AlterField(
            model_name='pony',
            name='file_name',
            field=models.CharField(verbose_name='file name', max_length=32),
        ),
        migrations.AlterField(
            model_name='pony',
            name='name',
            field=models.CharField(verbose_name='name', max_length=32),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(verbose_name='address', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_enabled',
            field=models.BooleanField(verbose_name='address enabled', default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_latitude',
            field=models.FloatField(null=True, verbose_name='latitude', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_longitude',
            field=models.FloatField(null=True, verbose_name='longitude', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=stdimage.models.StdImageField(null=True, upload_to=stdimage.utils.UploadToUUID(path='avatars'), verbose_name='avatar', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(150, message='The bio should be longer than 150 character')], verbose_name='bio'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(verbose_name='birthday'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthday_enabled',
            field=models.BooleanField(verbose_name='birthday enabled', default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(verbose_name='city', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='enabled',
            field=models.BooleanField(verbose_name='enabled', default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mail_enabled',
            field=models.BooleanField(verbose_name='mail enabled', default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name_enabled',
            field=models.BooleanField(verbose_name='name enabled', default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='phone', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_enabled',
            field=models.BooleanField(verbose_name='phone enabled', default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='postal_code',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message='The postal code must be 5 digits.', regex='^\\d[1-9]\\d{3}$')], verbose_name='postal code', max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(verbose_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userpony',
            name='message',
            field=models.CharField(verbose_name='message', max_length=64),
        ),
        migrations.AlterField(
            model_name='userpony',
            name='pony',
            field=models.ForeignKey(verbose_name='pony', to='users.Pony'),
        ),
        migrations.AlterField(
            model_name='userpony',
            name='profile',
            field=models.ForeignKey(verbose_name='profile', to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='userurl',
            name='icon',
            field=models.ForeignKey(verbose_name='icon', to='users.Icon'),
        ),
        migrations.AlterField(
            model_name='userurl',
            name='profile',
            field=models.ForeignKey(verbose_name='profil', to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='userurl',
            name='url',
            field=models.URLField(verbose_name='url'),
        ),
    ]
