#!/usr/bin/env python3

import csv
import sys
from collections import Counter 

f = open(sys.argv[1], 'r')

lines=f.readlines()

result=[]

for x in lines:
    result.append(x.split('|')[4])
f.close()

s = str(result).split()
b = Counter(s)

t10 = b.most_common(10)

for k,v in enumerate(t10):
     print(v)
