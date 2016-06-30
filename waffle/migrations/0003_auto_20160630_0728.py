# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waffle', '0002_auto_20160323_0812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flag',
            name='active_cookie_name',
        ),
        migrations.RemoveField(
            model_name='flag',
            name='active_cookie_value',
        ),
        migrations.RemoveField(
            model_name='flag',
            name='active_for_cookie',
        ),
    ]
