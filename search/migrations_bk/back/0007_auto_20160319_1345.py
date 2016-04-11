# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_varinfo_disease'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varinfo',
            name='disease',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
    ]
