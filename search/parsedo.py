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
#num=1
for line in dofile:
    if line.startswith('id:'):
        doid = line.strip().split()[1]
    if line.startswith('name:'):
        name = line.strip()[6:]
    if line.startswith('def:'):
        defi = line.strip()[5:].replace('"','').replace('\\','')
    if line.startswith('xref: OMIM'):
        omimid = line.strip().split()[1]
#        if omimid in ids:
        omim.append(omimid)
    if line.startswith('is_a:'):
        is_a = line.split()[1]
#        if len(omim):
        nodes.append(do(doid,name,defi,omim,is_a))
        omim=[]
#        num+=1

##looking for leaves that are in the final list
leaves=[]
for el in nodes:
    for i in el.omim:
        if i in ids:
            leaves.append(el)
            break

def loop(leaf,parents):
    if leaf.is_a == "DOID:4":
        return parents
    for node in nodes:
        if node.doid == leaf.is_a:
            parents.append(node)
            break
    return loop(node,parents)

fnodes=[]
for leaf in leaves:
    parents=loop(leaf,[leaf,])
    fnodes.extend(parents)
fnodes=set(fnodes)

print "["
num=1
for fnode in fnodes: 
    print "  {"
    print '    "model": "search.doinfo",'
    print '    "pk": '+str(num)+','
    print '    "fields": {'
    print '      "doid": '+ '"' + fnode.doid + '",'
    print '      "name": '+ '"' + fnode.name + '",'
    print '      "defi": '+ '"' + fnode.defi + '",'
    print '      "omim": '+ '"' + "+".join(fnode.omim) + '",'
    print '      "is_a": '+ '"' + fnode.is_a + '"'
    print '    }'
    print "  },"
    num+=1
print "]"
    
