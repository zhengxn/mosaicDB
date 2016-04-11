# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20160318_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='pubinfo',
            name='other_cases',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
