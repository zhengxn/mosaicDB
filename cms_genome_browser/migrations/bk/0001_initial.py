# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file
import filer.fields.image
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20160316_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Browser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Enter a brief, descriptive name for the browser.', unique=True, max_length=255, verbose_name=b'browser name')),
                ('description', models.TextField(help_text=b'Enter a description for the browser.', verbose_name=b'browser description', blank=True)),
                ('slug', models.SlugField(help_text=b'Enter a unique slug for this genome browser. This should get auto-generated.', unique=True, max_length=255, verbose_name=b'slug')),
                ('chr', models.CharField(help_text=b'The chromosome to display when the browser loads.', max_length=64, verbose_name=b'default chromosome')),
                ('start', models.IntegerField(help_text=b'The start position of range to display when the browser loads.', verbose_name=b'default start position', validators=[django.core.validators.MinValueValidator(1)])),
                ('end', models.IntegerField(help_text=b'The end position of range to display when the browser loads.', verbose_name=b'default end position', validators=[django.core.validators.MinValueValidator(1)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Genome Browser',
                'verbose_name_plural': 'Genome Browsers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoordSystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auth', models.CharField(help_text=b'Authority string used in the <a href="http://dasregistry.org/" target="_blank">DAS Registry</a>.', max_length=10, verbose_name=b'authority', blank=True)),
                ('version', models.CharField(help_text=b'Version string used in the <a href="http://dasregistry.org/" target="_blank">DAS Registry</a>.', max_length=10, verbose_name=b'version', blank=True)),
                ('ucsc_name', models.CharField(blank=True, help_text=b'UCSC genome browser name of the assembly, if defined in the list of <a href="https://genome.ucsc.edu/FAQ/FAQreleases.html#release1" target="_blank">UCSC genome releases</a>.', max_length=10, verbose_name=b'UCSC name', validators=[django.core.validators.RegexValidator(regex=b'^[a-z]{2}\\d+$|^[a-z]{3}[A-Z][a-z]{2}\\d+$', message=b"UCSC name must be of the format 'gs#' or 'gggSss#'.", code=b'invalid_UCSC_name')])),
            ],
            options={
                'ordering': ['species', 'auth', 'version'],
                'verbose_name': 'Coordinate System',
                'verbose_name_plural': 'Coordinate Systems',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Enter the species name.', max_length=255, verbose_name=b'species name')),
                ('taxid', models.IntegerField(help_text=b'Enter the Taxonomy ID for the species. Taxonomy names and IDs can be found at <a href="http://www.ncbi.nlm.nih.gov/taxonomy" target="_blank">NCBI</a>.', null=True, verbose_name=b'taxonomy ID', blank=True)),
            ],
            options={
                'ordering': ['name', 'taxid'],
                'verbose_name': 'Species',
                'verbose_name_plural': 'Species',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stylesheet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Enter a brief, descriptive name for this stylesheet.', unique=True, max_length=255, verbose_name=b'stylesheet name')),
                ('description', models.TextField(help_text=b'Describe the style this stylesheet provides.', verbose_name=b'stylesheet description', blank=True)),
                ('is_downloadable', models.BooleanField(default=True, help_text=b"Add download button for stylesheet file to the genome browser's info window.", verbose_name=b'stylesheet downloadable?')),
                ('style_type', models.CharField(help_text=b'Select the type of stylesheet being used.', max_length=4, verbose_name=b'stylesheet type', choices=[(b'XML', b'DAS XML Stylesheet'), (b'JSON', b'JSON-encoded Stylesheet')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('style_file', filer.fields.file.FilerFileField(related_name='cms_genome_browser_stylesheet_stylesheet', to='filer.File', help_text=b'Upload/select an image to represent this genome browser.select a stylesheet for the track. More info can be found in the <a href="https://www.biodalliance.org/stylesheets.html" target="_blank">Stylesheets for Dalliance</a> documentation.')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Stylesheet',
                'verbose_name_plural': 'Stylesheets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField()),
                ('name', models.CharField(help_text=b'Enter a brief name for the track.', max_length=64, verbose_name=b'track name')),
                ('description', models.CharField(help_text=b'Enter a short description for the track.', max_length=255, verbose_name=b'track description', blank=True)),
                ('track_type', models.CharField(help_text=b'Select the source type for this track.', max_length=20, verbose_name=b'track type', choices=[(b'BAM', b'BAM'), (b'BED', ((b'BED-MemStore', b'BED (MemStore)'), (b'BED-Tabix', b'BED (Tabix)'))), (b'bigWig', b'bigWig'), (b'bigBed', b'bigBed'), (b'DAS', ((b'DAS-feature', b'DAS (feature)'), (b'DAS-sequence', b'DAS (sequence)'))), (b'twoBit', b'twoBit'), (b'VCF', ((b'VCF-MemStore', b'VCF (MemStore)'), (b'VCF-Tabix', b'VCF (Tabix)'))), (b'WIG', b'WIG')])),
                ('collapse_super_groups', models.BooleanField(default=False, help_text=b"Attempt to allow more 'gene-like' rendering for some data sources.", verbose_name=b'CSG?')),
                ('provides_entrypoint', models.BooleanField(default=False, help_text=b'Does this track provide entry points? Entry points comprise the coordinate system on which annotations are made.', verbose_name=b'entry?')),
                ('pinned', models.BooleanField(default=False, help_text=b"'Pin' this trackc in the non-scrolling section at the top of the browser.", verbose_name=b'pin?')),
                ('is_downloadable', models.BooleanField(default=True, help_text=b"Add download button for data file to the genome browser's info window.", verbose_name=b'D/L?')),
                ('publish_track', models.BooleanField(default=True, help_text=b'Display track in the genome browser.', verbose_name=b'publish?')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('browser', models.ForeignKey(blank=True, to='cms_genome_browser.Browser', help_text=b'Specify genome browser this track belongs to.', null=True)),
                ('data_file', filer.fields.file.FilerFileField(related_name='cms_genome_browser_track_data', to='filer.File', help_text=b'Upload/select a data file for the track. More info can be found in the <a href="http://www.biodalliance.org/config-source.html" target="_blank">Configuring a source</a> documentation.')),
                ('index_file', filer.fields.file.FilerFileField(related_name='cms_genome_browser_track_index', blank=True, to='filer.File', help_text=b"<strong>If data file is a BAM or Tabix file</strong>, upload/select an index file (.bai or .tbi) that corresponds to the track's BAM/Tabix file.", null=True)),
                ('stylesheet', models.ForeignKey(blank=True, to='cms_genome_browser.Stylesheet', help_text=b'Choose a stylesheet to add cusom styles to this track.', null=True)),
            ],
            options={
                'ordering': ['browser', 'order'],
                'verbose_name': 'Track',
                'verbose_name_plural': 'Tracks',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coordsystem',
            name='species',
            field=models.ForeignKey(help_text=b'Select a species. Taxonomy ID is shown in parentheses, if present.', to='cms_genome_browser.Species'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='browser',
            name='coordinate_system',
            field=models.ForeignKey(help_text=b'Select a coordinate system. Taxonomy ID, authority, version, and UCSC name are shown in parentheses, if present.', to='cms_genome_browser.CoordSystem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='browser',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='cms_genome_browser_browser_browser_image', blank=True, to='filer.Image', help_text=b'Upload/select an image to represent this genome browser.', null=True),
            preserve_default=True,
        ),
    ]
