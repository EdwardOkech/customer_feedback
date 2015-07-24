# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfback', '0006_auto_20150710_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, null=True, choices=[(0, b'Pending'), (1, b'Resolved')]),
        ),
    ]
