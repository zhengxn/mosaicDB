# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('varid', models.IntegerField(serialize=False, primary_key=True)),
                ('gene', models.CharField(max_length=30)),
                ('chrom', models.CharField(max_length=4)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('disease', models.CharField(max_length=100)),
                ('method', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
