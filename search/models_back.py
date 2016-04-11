from __future__ import unicode_literals

from django.db import models

class Variant(models.Model):
    varid = models.IntegerField(primary_key=True)
    gene = models.CharField(max_length=30)
    chrom = models.CharField(max_length=4)
    start = models.IntegerField()
    end = models.IntegerField()
    disease = models.CharField(max_length=100)
    method = models.CharField(max_length=50)
