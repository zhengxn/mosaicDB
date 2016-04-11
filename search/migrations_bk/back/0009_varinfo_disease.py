# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_remove_varinfo_diseases'),
    ]

    operations = [
        migrations.AddField(
            model_name='varinfo',
            name='disease',
            field=models.CharField(default='unknown', max_length=100),
            preserve_default=False,
        ),
    ]
