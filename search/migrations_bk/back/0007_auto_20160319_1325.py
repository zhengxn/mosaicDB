# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_varinfo_diseases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varinfo',
            name='diseases',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
