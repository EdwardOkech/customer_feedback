# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cfback', '0009_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('pic', models.ImageField(upload_to=b'cfback/team')),
                ('position', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=75)),
                ('twitter', models.URLField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Team',
            },
        ),
    ]
