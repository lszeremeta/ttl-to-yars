#!/usr/bin/env python
import rdflib
import string
import hashlib
import sys
from urlparse import urlparse
g=rdflib.Graph()
g.parse(sys.argv[1], format="turtle")
i = 0
for s,p,o in g:
  sh = hashlib.md5(s).hexdigest()
  t1 = urlparse(s)
  if t1.netloc!='':
    shu = "(" + sh[:32] + "{v:'<" + s + ">'})"
  else:
    shu = "(" + sh[:32] + "{v:'" + s + "'})"
  oh = hashlib.md5(o).hexdigest()
  t2 = urlparse(o)
  if t2.netloc!='':
    ohu = "(" + oh[:32] + "{v:'<" + o + ">'})"
  else:
    ohu = "(" + oh[:32] + "{v:'" + o + "'})"
  print shu
  print ohu
  print "(" + sh[:32] + ")-[" + p + "]->(" + oh[:32] + ")"

