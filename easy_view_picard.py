#!/home/kirill/Downloads/Python-3.6.7/python
# -*- coding: iso-8859-15 -*-

# commenting my code

import sys

f = sys.argv[1]

a = None
b = None

with open(f) as handler:
    for  i in handler:
        line = i.strip()
        if line.startswith("#") or not line:
            continue
        if not a:
            a = line
        else:
            b = line

a = a.split("\t")
b = b.split("\t")

d = dict(zip(a,b))

for k,v in d.items():
    print('\t'.join((k,v)))
