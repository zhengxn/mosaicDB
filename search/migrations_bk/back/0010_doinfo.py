# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_auto_20160320_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='doinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doid', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('defi', models.CharField(max_length=500)),
                ('omim', models.CharField(max_length=200)),
                ('is_a', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
