#!/usr/bin/env python3

import datetime
import os
import random
import sys
import time
import itertools
import re


N = 10000
d = '20130101'
t1 = datetime.time(9, 0, 0)
t2 = datetime.time(11, 59, 59)
sR = ["OK", "TEMP", "PERM"]
L = 500
f = 'X'

def time_in_range(low, high, interval):
    low = datetime.timedelta(hours=low.hour, minutes=low.minute, seconds=low.second)
    high = datetime.timedelta(hours=high.hour, minutes=high.minute, seconds=high.second)
    delta = (high - low).total_seconds()
    return low + datetime.timedelta(seconds=random.randrange(0, int(delta), interval))

def xfill(a):

    t = (time_in_range(t1, t2, 1))
    pid = (random.randint(3000,5000))
    s = random.choice(sR)
    data = random.choice(a).rstrip()
    o = open(sys.argv[2], 'a') 


    l1 = d + "|" + str(t) + "|" + str(pid) + "|" + s + "|"  + data + "|"

    if (len(l1)) > 500:
        r=(random.randint(100,300))
        data = data[:r].rsplit(' ', 1)[0]
        l2 = d + "|" + str(t) + "|" + str(pid) + "|" + s + "|"  + data + "|"
        filler = (500 - len(l2))
        l2 = l2 + f*(filler -1) + "\n"
        o.writelines(l2)
    else:
        filler = (500 - len(l1))
        l1 = l1 + f*(filler -1) + "\n"
        o.writelines(l1)
    o.close()

lines = tuple(open(sys.argv[1], 'r'))

for _ in itertools.repeat(None, N):
    xfill(lines)
