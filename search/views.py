import re
import operator
import sys

from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template.loader import get_template
from django.db.models import Q

from .models import Variant, Varinfo, pubinfo, indinfo, geneinfo, doinfo

def home(request):
    t = get_template('index.html')
#    return HttpResponse(t.render())
    return render_to_response('index.html')

def viewvar(request):
    if 'query' in request.GET:
        query = request.GET['query']
        pattern = re.compile("chr", re.IGNORECASE)
        if request.GET['query']=='':
            return HttpResponseRedirect('/')
        elif re.match('^[0-9|X|Y|x|y|]+:[0-9]+-[0-9]+$',pattern.sub('',query)):
            newquery = pattern.sub('',query)
            chrom = newquery.split(':')[0]
            start,end = newquery.split(':')[1].split('-')
            vars = Varinfo.objects.filter(Q(chrom__exact=chrom) & Q(start__gte=int(start)) & Q(end__lte=int(end))).select_related('entrez')
        else:
            filters=[]
            for key in re.split('[\s-]',query):
                filters.append(Q(indid__disease__icontains=key))
            vars = Varinfo.objects.filter(Q(gene__icontains=query)|reduce(operator.and_, filters)|Q(indid__mosaic__method__icontains=query)|Q(entrez__entrez__contains=query)).select_related('entrez').distinct()
    return render_to_response('search_results.html',{'variants':vars,'query':query})

def varpage(request,varid):
    var = Varinfo.objects.get(Q(varid__exact=varid))
    dblinks = var.entrez.other_ids
    dblinks = re.sub('[\[\]\'u\s]','',dblinks)
    out = {}
    flag = 0
    for i in dblinks.split(','):
        if not flag:
            out[i]=''
            key = i
        else:
            if key == 'HGNC':
                out[key]=[i,'http://www.genenames.org/cgi-bin/gene_symbol_report?hgnc_id='+i]
            elif key == 'Ensembl':
                out[key]=[i,'http://asia.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g='+i]
            elif key == 'MIM':
                out[key]=[i,'http://www.omim.org/entry/'+i]
            elif key == 'HPRD':
                out[key]=[i,'http://www.hprd.org/protein/'+i]
            elif key == 'Vega':
                out[key]=[i,'http://vega.sanger.ac.uk/id/'+i]
            else:
                out[key]=[i,'#']
            flag=-1
        flag+=1
    names = var.entrez.other_names
    names = re.sub('[\[\]\'u\s]','',names)
    names = names.split(',')
    entrez = var.entrez.entrez
    varnum = Varinfo.objects.filter(entrez=entrez).count() 
    return render_to_response('variant.html', {'variant':var, 'dblinks':out, 'names':names, 'genecount':varnum,})

def genpage(request,entrez):
    gen = geneinfo.objects.get(Q(entrez__exact=entrez))
    vars = Varinfo.objects.filter(Q(entrez__entrez__exact=entrez))
    dblinks = gen.other_ids
    dblinks = re.sub('[\[\]\'u\s]','',dblinks)
    out = {}
    flag = 0
    for i in dblinks.split(','):
        if not flag:
            out[i]=''
            key = i
        else:
            if key == 'HGNC':
                out[key]=[i,'http://www.genenames.org/cgi-bin/gene_symbol_report?hgnc_id='+i]
            elif key == 'Ensembl':
                out[key]=[i,'http://asia.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g='+i]
            elif key == 'MIM':
                out[key]=[i,'http://www.omim.org/entry/'+i]
            elif key == 'HPRD':
                out[key]=[i,'http://www.hprd.org/protein/'+i]
            elif key == 'Vega':
                out[key]=[i,'http://vega.sanger.ac.uk/id/'+i]
            else:
                out[key]=[i,'#']
            flag=-1
        flag+=1
    names = gen.other_names
    names = re.sub('[\[\]\'u\s]','',names)
    names = names.split(',')
    return render_to_response('gene.html',{'gene':gen, 'variants':vars, 'dblinks':out, 'names':names,})

def indpage(request,indid):
    ind = indinfo.objects.get(Q(indid__exact=indid))
    vars = Varinfo.objects.filter(Q(indid__indid__exact=indid))
    return render_to_response('individual.html',{'ind':ind, 'variants':vars,})

def dispage(requst,omim):
    vars = Varinfo.objects.filter(Q(indid__omim__exact=omim)).distinct()
    disease = indinfo.objects.filter(Q(omim__exact=omim))[0].disease
    return render_to_response('disease.html',{'variants':vars,'disease':disease,'omim':omim})

def addpage(request):
    return render(request, 'add.html')

def ajax_list(request):
    num = request.GET['a']
    a = range(int(num))
    return JsonResponse(a, safe=False)

def menupage(request):
    doid = 'DOID:4'
    roots = doinfo.objects.filter(Q(is_a=doid))
    menu = ''
    for root in roots:
        menu += ulunit(root)
    return render_to_response('treemenu.html',{'menu':menu})

def ulunit(father):
    dos = doinfo.objects.filter(Q(is_a=father.doid))
    if not dos:
        return '<li id="'+father.doid +'">'+father.name+'</li>\n'
    else:
        header = '<li id="'+father.doid +'">'+father.name +'\n<ul>'
        footer = '</ul>\n</li>\n'
        a = header
        for do in dos:
            a+=ulunit(do)
    return a+footer

def menu(request):
#    if request.is_ajax():
#        doid = request.GET.get('doid')
#        if doid is None:
#            return    
    doid = request.GET['doid']
    thisone = doinfo.objects.get(Q(doid=doid))
    defi = re.sub("\[.+\]",'',thisone.defi)
    defi = re.sub('_','',defi)
    sys.stderr.write(thisone.name)
    if doinfo.objects.filter(Q(is_a=doid)).exists():
        vars=[]
    else:
        omims = thisone.omim.split('+')
        filters = []
        for omim in omims:
            filters.append(Q(indid__omim__exact=omim[5:]))
        vars = Varinfo.objects.filter(reduce(operator.or_, filters)).select_related('indid')
    template = 'variants_table.html'
    data={
    'names':thisone,
    'variants': vars,
    'defi': defi,
    }
    return render_to_response(template, data)
