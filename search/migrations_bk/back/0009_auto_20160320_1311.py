# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_auto_20160319_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varinfo',
            name='entrez',
            field=models.ForeignKey(to='search.geneinfo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='varinfo',
            name='indid',
            field=models.ForeignKey(to='search.indinfo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='varinfo',
            name='pmid',
            field=models.ForeignKey(to='search.pubinfo'),
            preserve_default=True,
        ),
    ]
