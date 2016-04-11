# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20160319_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varinfo',
            name='cdna_position',
            field=models.CharField(default='', max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
