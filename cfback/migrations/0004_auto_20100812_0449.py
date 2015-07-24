# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfback', '0003_auto_20100814_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date posted'),
        ),
    ]
