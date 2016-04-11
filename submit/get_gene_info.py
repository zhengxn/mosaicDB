#!/usr/bin/python

import urllib2
import xmltodict
import collections
import sys

def homepage(id):
    file = urllib2.urlopen('http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=gene&id=' + str(id) + '&retmode=xml')
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    return data

def printdict(dict, li):
    if type(dict) is collections.OrderedDict:
        for key in dict.keys():
            printdict(dict[key],li)
    elif type(dict) is list:
        for i in dict:
            printdict(i,li)
    else:
        li.append(dict)
    return li

def get_info(entrez):
    dict = {}
    dict['entrez'] = entrez
    data = homepage(entrez)['Entrezgene-Set']['Entrezgene']
    dict['symbol']=data['Entrezgene_gene']['Gene-ref'].get('Gene-ref_locus','None')
    dict['full_name']=data['Entrezgene_gene']['Gene-ref'].get('Gene-ref_desc','None')
    dict['location']=data['Entrezgene_gene']['Gene-ref'].get('Gene-ref_maploc','None')
    dbs=[]
    dict['ids']=printdict(data['Entrezgene_gene']['Gene-ref'].get('Gene-ref_db','None'),dbs)
    names=[]
    dict['names']=printdict(data['Entrezgene_gene']['Gene-ref'].get('Gene-ref_syn','None'),names)
    dict['summary']=data.get('Entrezgene_summary','None')
    return dict

if __name__=="__main__":
    print get_info(22931).keys()
    sys.exit()
    data = homepage(22931)['Entrezgene-Set']['Entrezgene']
    print 22931  ##entrezid
    print data['Entrezgene_gene']['Gene-ref']['Gene-ref_locus'] ##official symbol
    print data['Entrezgene_gene']['Gene-ref']['Gene-ref_desc']  ##Official full name
    print data['Entrezgene_gene']['Gene-ref']['Gene-ref_maploc'] ##location
#    print "Other ids:",
    dbs = []
    print printdict(data['Entrezgene_gene']['Gene-ref']['Gene-ref_db'],dbs)
#    print
#    print "Also known as:", 
    names = []
    print printdict(data['Entrezgene_gene']['Gene-ref']['Gene-ref_syn'],names)
#    print
#    print "Summary:",
    print data['Entrezgene_summary']
#    print
#    printdict(homepage(22941)['Entrezgene-Set']['Entrezgene']['Entrezgene_gene'])
