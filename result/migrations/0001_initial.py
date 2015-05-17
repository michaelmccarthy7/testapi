# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pps', models.CharField(max_length=100)),
                ('minor_code', models.CharField(max_length=100)),
                ('award_code', models.CharField(max_length=100)),
                ('class_code', models.CharField(max_length=100)),
                ('award', models.CharField(max_length=100)),
            ],
        ),
    ]
