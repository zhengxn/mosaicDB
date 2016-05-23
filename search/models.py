from __future__ import unicode_literals

from django.db import models

class Variant(models.Model):
    class Meta:
        managed=False
    varid = models.IntegerField(primary_key=True)
    gene = models.CharField(max_length=30)
    chrom = models.CharField(max_length=5)
    start = models.IntegerField()
    end = models.IntegerField()
    disease = models.CharField(max_length=100)
    method = models.CharField(max_length=50)

class pubinfo(models.Model):
    class Meta:
        managed=False
    pmid = models.IntegerField(primary_key=True,unique=True)
    title = models.CharField(max_length=200)
    journal = models.CharField(max_length=100)
    date = models.CharField(max_length=10)
    disease = models.CharField(max_length=50)
    population = models.CharField(max_length=50, blank=True, default='')
    incidence_lower = models.CharField(max_length=50, blank=True, default='')
    incidence_higher = models.CharField(max_length=50, blank=True, default='')
    male_cases = models.IntegerField(null=True, blank=True)
    female_cases = models.IntegerField(null=True, blank=True)
    other_cases = models.IntegerField(null=True, blank=True)
    paternal_age_effect = models.CharField(max_length=50, blank=True,default='')
 #   note = models.CharField(max_length=500, blank=True)

class indinfo(models.Model):
    class Meta:
        managed=False
    indid = models.CharField(max_length=20,primary_key=True,unique=True)
    pmid = models.IntegerField()
    whose_mosaic = models.CharField(max_length=10)
    patient_mosaic_origin = models.CharField(max_length=10, blank=True,default='')
    phenotype_mosaic = models.IntegerField()
    age_lower = models.FloatField(null=True, blank=True)
    age_upper = models.FloatField(null=True, blank=True)
    affected_child_nc = models.IntegerField(null=True, blank=True)
    affected_male_child_nc = models.IntegerField(null=True, blank=True)
    affected_female_child_nc = models.IntegerField(null=True, blank=True)
    affected_grandson = models.IntegerField(null=True, blank=True)
    affected_granddaughter = models.IntegerField(null=True, blank=True)
    disease = models.CharField(max_length=50)
    omim = models.IntegerField()

class geneinfo(models.Model):
    class Meta:
        managed=False
    entrez = models.IntegerField(primary_key=True,unique=True)
    symbol = models.CharField(max_length=20)
    fullname = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    other_ids = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100)
    summary = models.CharField(max_length=1000)

class Varinfo(models.Model):
    class Meta:
        managed=False
    varid = models.AutoField(primary_key=True)
    indid = models.ManyToManyField(indinfo)
    entrez = models.ForeignKey(geneinfo)
    pmid = models.ManyToManyField(pubinfo)
    gene = models.CharField(max_length=30)
    chrom = models.CharField(max_length=5)
    start = models.IntegerField()
    end = models.IntegerField()
    dna_ref_nt = models.CharField(max_length=30)
    dna_alt_nt = models.CharField(max_length=30)
    hgvs = models.CharField(max_length=100,unique=True)
    genome_assembly = models.CharField(max_length=10)
    exon_intron = models.CharField(max_length=10)
    exon_number = models.CharField(max_length=10, blank=True, default='')
    exon_nc = models.CharField(max_length=10, blank=True, default='')
    protein_position = models.IntegerField(null=True, blank=True)
    pro_ref_aa = models.CharField(max_length=10, blank=True, default='')
    pro_alt_aa = models.CharField(max_length=10, blank=True, default='')
    frameshift = models.CharField(max_length=10, blank=True, default='')
    aa_indel = models.CharField(max_length=30, blank=True, default='')
    cdna_position = models.CharField(max_length=10, blank=True, default='')
    cdna_ref_aa = models.CharField(max_length=10, blank=True, default='')
    cdna_alt_aa = models.CharField(max_length=10, blank=True, default='')
    nt_indel = models.CharField(max_length=30, blank=True, default='')
    mrna_accession = models.CharField(max_length=30)
    mrna_length = models.IntegerField(null=True)
    ref_length = models.IntegerField(null=True)
    disease = models.CharField(max_length=100, null=True)


class mosaic(models.Model):
    id = models.AutoField(primary_key=True)
    ind = models.ForeignKey(indinfo)
    af_lower = models.FloatField(null=True, blank=True)
    af_upper = models.FloatField(null=True, blank=True)
    total_red = models.IntegerField(null=True, blank=True)
    sample_type = models.CharField(max_length=30)
    method = models.CharField(max_length=30)
    var = models.ForeignKey(Varinfo)
    
class doinfo(models.Model):
    class Meta:
        managed=False
    doid = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    defi = models.CharField(max_length=500)
    omim = models.CharField(max_length=200)
    is_a = models.CharField(max_length=30)
