# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waffle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='active_cookie_name',
            field=models.CharField(blank=True, help_text='The name of the cookie to look for if active_for_cookie isset.', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='flag',
            name='active_cookie_value',
            field=models.CharField(blank=True, help_text='The value of the specified cookie - true for all valuesif left blank.', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='flag',
            name='active_for_cookie',
            field=models.BooleanField(default=False, help_text='Activate this flag if the user has a cookie set with the specifiedname and value.'),
        ),
    ]
