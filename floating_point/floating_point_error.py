# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 23:12:13 2018

@author: Marcus
"""

import numpy as np

x_start = np.float32(1.0)

x = x_start
N = 10000

r_start = np.float32(0.0)
r_end = np.float32(2000.0)

print(x)

for n in range(N):
    a = np.float32(np.random.uniform(r_start, r_end))
    b = np.float32(np.random.uniform(r_start, r_end))
    
    x += a
    x += b
    
    x -= a
    x -= b
    
print(x_start - x)