#!/usr/bin/python

import sys
from search.models import Variant, Varinfo, pubinfo, indinfo, geneinfo
from get_gene_info import get_info 

def insert(f):
    file = ''
    for chunk in f.chunks():
        for line in chunk.split('\n'):
            if len(line.split()) > 0:
                ind, varid, gene, chrom, start, end, met, dis = line.split()
                item = Variant(varid=varid,gene=gene,chrom=chrom,start=start,end=end,disease=dis,method=met)
                item.save()
            else:
                continue
    return "Insert successfully!"

def intnone(str):
    return bool(str) and int(str) or None

def floatnone(str):
    return bool(str) and float(str) or None

def var(f):
    num = 0
    for chunk in f.chunks():
        for line in chunk.split('\n'):
            if len(line.split('\t')) >= 33:
                if line.startswith('V'):
                    continue
                sys.stderr.write(line)
                varid, indid, entrez, pmid, gene, chrom, start, end, dna_ref_nt, dna_alt_nt, hgvs, genome_assembly, exon_intron, exon_number, exon_nc, protein_position, pro_ref_aa, pro_alt_aa, frameshift, aa_indel, cdna_position, cdna_ref_aa, cdna_alt_aa, nt_indel, mrna_accession, mrna_length, ref_length, af_lower, af_upper, total_red, sample_type, method, disease = line.split('\t')[0:33]
                var_set = Varinfo.objects.filter(varid = int(varid))
                indidi = indinfo.objects.get(indid=indid)
                entrezi = geneinfo.objects.get(entrez=int(entrez))
                pmidi = pubinfo.objects.get(pmid=int(pmid))
                if not var_set.exists():
                    item = Varinfo(varid=int(varid), indid=indidi,entrez=entrezi, pmid=pmidi, gene=gene, chrom=chrom, start=int(start), end=int(end), dna_ref_nt=dna_ref_nt, dna_alt_nt=dna_alt_nt, hgvs=hgvs, genome_assembly=genome_assembly, exon_intron=exon_intron, exon_number=exon_number, exon_nc=exon_nc, protein_position=intnone(protein_position), pro_ref_aa=pro_ref_aa, pro_alt_aa=pro_alt_aa, frameshift=frameshift, aa_indel=aa_indel, cdna_position=cdna_position, cdna_ref_aa=cdna_ref_aa, cdna_alt_aa=cdna_alt_aa, nt_indel=nt_indel, mrna_accession=mrna_accession, mrna_length=intnone(mrna_length), ref_length=intnone(ref_length), af_lower=floatnone(af_lower), af_upper=floatnone(af_upper), total_red=intnone(total_red), sample_type=sample_type, method=method, disease=disease)
                    item.save()
                    num+=1
                gene_set = geneinfo.objects.filter(entrez=int(entrez))
                if gene_set.exists():
                    continue
                gene_info = get_info(entrez)
                symbol = gene_info.get('symbol','None')
                full_name = gene_info.get('full_name', 'None')
                ids = gene_info.get('ids', 'None')
                location = gene_info.get('location','None')
                names = gene_info.get('names','None')
                summary = gene_info.get('summary', 'None')
                item = geneinfo(entrez=int(entrez),symbol=symbol,fullname=full_name,location=location,other_ids=ids,other_names=names,summary=summary)
                item.save()
            else:
                continue
    return "Insert %d variants successfully!" %(num,)

def pub(f):
    num = 0
    for chunk in f.chunks():
        for line in chunk.split("\n"):
            if len(line.split('\t')) >= 12:
                if line.startswith('P'):
                    continue
                sys.stderr.write(line)
                pmid, title, journal, date, disease, population, incidence_lower, incidence_upper, male_cases, female_cases, other_cases, paternal_age_effect = line.split('\t')[0:12]
                pub_set = pubinfo.objects.filter(pmid=int(pmid))
                if pub_set.exists():
                    continue
                item = pubinfo(pmid=int(pmid), title=title, journal=journal, date=date, disease=disease, population=population, incidence_lower=incidence_lower, incidence_higher=incidence_upper, male_cases=intnone(male_cases), female_cases=intnone(female_cases), other_cases=intnone(other_cases), paternal_age_effect=paternal_age_effect)
                item.save()
                num+=1
            else:
                continue
    return "Insert %d publications successfully!" %(num, )

def ind(f):
    num = 0
    for chunk in f.chunks():
        for line in chunk.split('\n'):
            print len(line.split('\t'))
            if len(line.split('\t')) >= 14:
                if line.startswith('I'):
                    continue
                sys.stderr.write(line)
                indid, pmid, whose_mosaic, patient_mosaic_origin, phenotype_mosaic, age_lower, age_upper, affected_child_nc, affected_male_child_nc, affected_female_child_nc, affected_grandson, affected_granddaughter, disease, omim = line.split('\t')[0:14]
                ind_set = indinfo.objects.filter(indid=indid)
                if ind_set.exists():
                    continue
                item = indinfo(indid=indid, pmid=int(pmid), whose_mosaic=whose_mosaic, patient_mosaic_origin=patient_mosaic_origin, phenotype_mosaic=phenotype_mosaic, age_lower=floatnone(age_lower), age_upper=floatnone(age_upper), affected_child_nc=intnone(affected_child_nc), affected_male_child_nc=intnone(affected_male_child_nc), affected_female_child_nc=intnone(affected_female_child_nc), affected_grandson=intnone(affected_grandson), affected_granddaughter=intnone(affected_granddaughter), disease=disease, omim=int(omim))
                item.save()
                num+=1
            else:
                continue
    return "Insert %d individuals successfully!" %(num, )

