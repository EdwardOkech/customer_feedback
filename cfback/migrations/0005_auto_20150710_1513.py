# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfback', '0004_auto_20100812_0449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'permissions': (('can_delete_feedbacks', 'Can delete feedbacks'), ('can_view_feedbacks', 'Can view feedbacks'))},
        ),
    ]
