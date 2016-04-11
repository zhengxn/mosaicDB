#!/usr/bin/python
import sys

dofile = open(sys.argv[1],'r')
omimid = open(sys.argv[2],'r')

ids=[]
for line in omimid:
    ids.append("OMIM:"+line.strip())

class do(object):
    def __init__(self,doid,name,defi,omim,is_a):
        self.doid = doid
        self.name = name
        self.defi = defi
        self.omim = omim
        self.is_a = is_a

omim = []
nodes = []
print "["
num=1
for line in dofile:
    if line.startswith('id:'):
        doid = line.strip().split()[1]
    if line.startswith('name:'):
        name = line.strip()[6:]
    if line.startswith('def:'):
        defi = line.strip()[5:].replace('"','').replace('\\','')
    if line.startswith('xref: OMIM'):
        omimid = line.strip().split()[1]
        if omimid in ids:
            omim.append(omimid)
    if line.startswith('is_a:'):
        is_a = line.split()[1]
        if len(omim):
            print "  {"
            print '    "model": "search.doinfo",'
            print '    "pk": '+str(num)+','
            print '    "fields": {'
            print '      "doid": '+ '"' + doid + '",'
            print '      "name": '+ '"' + name + '",'
            print '      "defi": '+ '"' + defi + '",'
            print '      "omim": '+ '"' + "+".join(omim) + '",'
            print '      "is_a": '+ '"' + is_a + '"'
            print '    }'
            print "  },"
#            print "INSERT INTO doinfo (doid,name,defi,omim,is_a) VALUES (%s,%s,%s,%s,%s);" %(doid,name,defi,"+".join(omim),is_a)
#            nodes.append(do(doid,name,defi,omim,is_a))
            omim=[]
            num+=1
print "]"
#for el in nodes:
    
