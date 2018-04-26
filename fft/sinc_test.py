# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 00:27:51 2018

@author: Marcus
"""

import numpy as np
import pylab as plt

db_magnitude = False

N = 6400

n_sidelobes = 10

centre = 4000

failures = []

k = centre
comp = N - 1 - k

lower = -1 - n_sidelobes
upper = -1 * lower

lower *= (k / N)
upper *= (comp / N)

t = np.linspace(lower, upper, N)

sinc = np.abs(np.sinc(t))

if(db_magnitude):
    sinc = 20 * np.log10(sinc)
    
if(np.argmax(sinc) != centre):
    failures.append([np.argmax(sinc), centre])

plt.plot(sinc)
plt.show()
print(np.argmax(sinc))
print(np.max(sinc))