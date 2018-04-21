# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 21:52:03 2018

@author: Marcus
"""

import numpy as np
import pylab as plt
from matplotlib import collections as matcoll

#FFT leakage

complex_in = True
plot = True

N = 64
fs = 1
ts = 1/fs
A0 = 1

t = np.linspace(0, (N - 1) * ts, N)

m = 37
f = m * fs / N
w = 2 * np.pi * f

if(complex_in):
    x = np.cos(w * t) + 1j*np.sin(w * t)
else:
    x = np.sin(w * t)

x *= A0

f_out = np.abs(np.fft.fft(x))
frequencies = np.fft.fftfreq(N, d=ts)

if(plot):
    #plt.plot(frequencies, f_out)
    plt.stem(f_out, markerfmt='b.')
    
    plt.show()
    
    print(max(f_out))