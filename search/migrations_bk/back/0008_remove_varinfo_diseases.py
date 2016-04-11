# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20160319_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='varinfo',
            name='diseases',
        ),
    ]
