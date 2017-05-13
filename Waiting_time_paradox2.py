# -*- coding: utf-8 -*-
"""
Created on Sat May 13 05:10:14 2017

@author: lenovo
"""

import numpy as np
import random as rd
import math

sx = 0
sr = 0
si = 0
c = 0
times = 10000

for i in range(times):
    s = 0
    t = 300 - 200 * math.log(rd.random())
    while 1:
        x = np.random.exponential(10)
        s = s + x
        c += 1
        sx = sx + x
        if s > t:
            si += x
            sr += s - t
            break
        
print(sx/c, sr/times, si/times)