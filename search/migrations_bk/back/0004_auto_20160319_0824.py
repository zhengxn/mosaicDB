# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_pubinfo_other_cases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varinfo',
            name='exon_nc',
            field=models.CharField(default='', max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='varinfo',
            name='exon_number',
            field=models.CharField(default='', max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
