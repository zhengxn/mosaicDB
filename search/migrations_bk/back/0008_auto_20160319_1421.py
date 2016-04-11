# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20160319_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varinfo',
            name='indid',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
