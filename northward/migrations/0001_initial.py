# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MigrationHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_name', models.CharField(max_length=255)),
                ('migration', models.CharField(max_length=255)),
                ('applied', models.DateTimeField(blank=True)),
            ],
            options={
                'db_table': 'south_migrationhistory',
            },
        ),
    ]
