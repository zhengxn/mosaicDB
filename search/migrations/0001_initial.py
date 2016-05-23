# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doid', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('defi', models.CharField(max_length=500)),
                ('omim', models.CharField(max_length=200)),
                ('is_a', models.CharField(max_length=30)),
            ],
            options={
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='geneinfo',
            fields=[
                ('entrez', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('symbol', models.CharField(max_length=20)),
                ('fullname', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=20)),
                ('other_ids', models.CharField(max_length=100)),
                ('other_names', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=1000)),
            ],
            options={
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='indinfo',
            fields=[
                ('indid', models.CharField(max_length=20, unique=True, serialize=False, primary_key=True)),
                ('pmid', models.IntegerField()),
                ('whose_mosaic', models.CharField(max_length=10)),
                ('patient_mosaic_origin', models.CharField(default='', max_length=10, blank=True)),
                ('phenotype_mosaic', models.IntegerField()),
                ('age_lower', models.FloatField(null=True, blank=True)),
                ('age_upper', models.FloatField(null=True, blank=True)),
                ('affected_child_nc', models.IntegerField(null=True, blank=True)),
                ('affected_male_child_nc', models.IntegerField(null=True, blank=True)),
                ('affected_female_child_nc', models.IntegerField(null=True, blank=True)),
                ('affected_grandson', models.IntegerField(null=True, blank=True)),
                ('affected_granddaughter', models.IntegerField(null=True, blank=True)),
                ('disease', models.CharField(max_length=50)),
                ('omim', models.IntegerField()),
            ],
            options={
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='pubinfo',
            fields=[
                ('pmid', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('journal', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=10)),
                ('disease', models.CharField(max_length=50)),
                ('population', models.CharField(default='', max_length=50, blank=True)),
                ('incidence_lower', models.CharField(default='', max_length=50, blank=True)),
                ('incidence_higher', models.CharField(default='', max_length=50, blank=True)),
                ('male_cases', models.IntegerField(null=True, blank=True)),
                ('female_cases', models.IntegerField(null=True, blank=True)),
                ('other_cases', models.IntegerField(null=True, blank=True)),
                ('paternal_age_effect', models.CharField(default='', max_length=50, blank=True)),
            ],
            options={
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('varid', models.IntegerField(serialize=False, primary_key=True)),
                ('gene', models.CharField(max_length=30)),
                ('chrom', models.CharField(max_length=5)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('disease', models.CharField(max_length=100)),
                ('method', models.CharField(max_length=50)),
            ],
            options={
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Varinfo',
            fields=[
                ('varid', models.AutoField(serialize=False, primary_key=True)),
                ('gene', models.CharField(max_length=30)),
                ('chrom', models.CharField(max_length=5)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('dna_ref_nt', models.CharField(max_length=30)),
                ('dna_alt_nt', models.CharField(max_length=30)),
                ('hgvs', models.CharField(unique=True, max_length=100)),
                ('genome_assembly', models.CharField(max_length=10)),
                ('exon_intron', models.CharField(max_length=10)),
                ('exon_number', models.CharField(default='', max_length=10, blank=True)),
                ('exon_nc', models.CharField(default='', max_length=10, blank=True)),
                ('protein_position', models.IntegerField(null=True, blank=True)),
                ('pro_ref_aa', models.CharField(default='', max_length=10, blank=True)),
                ('pro_alt_aa', models.CharField(default='', max_length=10, blank=True)),
                ('frameshift', models.CharField(default='', max_length=10, blank=True)),
                ('aa_indel', models.CharField(default='', max_length=30, blank=True)),
                ('cdna_position', models.CharField(default='', max_length=10, blank=True)),
                ('cdna_ref_aa', models.CharField(default='', max_length=10, blank=True)),
                ('cdna_alt_aa', models.CharField(default='', max_length=10, blank=True)),
                ('nt_indel', models.CharField(default='', max_length=30, blank=True)),
                ('mrna_accession', models.CharField(max_length=30)),
                ('mrna_length', models.IntegerField(null=True)),
                ('ref_length', models.IntegerField(null=True)),
                ('disease', models.CharField(max_length=100, null=True)),
            ],
            options={
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='mosaic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('af_lower', models.FloatField(null=True, blank=True)),
                ('af_upper', models.FloatField(null=True, blank=True)),
                ('total_red', models.IntegerField(null=True, blank=True)),
                ('sample_type', models.CharField(max_length=30)),
                ('method', models.CharField(max_length=30)),
                ('ind', models.ForeignKey(to='search.indinfo')),
                ('var', models.ForeignKey(to='search.Varinfo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
