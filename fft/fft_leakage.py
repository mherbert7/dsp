# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 21:52:03 2018

@author: Marcus
"""

import numpy as np
import pylab as plt

#FFT Leakage Script
#If m is not an integer, then leakage will be observed

complex_in = True
db_magnitude = False
plot = True

N = 64
fs = 0.4
ts = 1/fs
A0 = 1

n = np.linspace(0, N - 1, N)
#n = np.arange(0, N * ts, ts) #<- This is an equivalent way to generate t

m = 31
f = m * fs / N
w = 2 * np.pi * f

if(complex_in):
    x = np.cos(w * n * ts) + 1j*np.sin(w * n * ts)
else:
    x = np.sin(w * n * ts)

x *= A0

f_out = np.abs(np.fft.fft(x))
frequencies = np.fft.fftfreq(N, d=ts)


if(db_magnitude):
    f_out = 20 * np.log10(f_out)

if(plot):
    plt.stem(f_out, markerfmt='b.')
    plt.title("FFT Output")
    plt.xlabel("Frequency index")
    plt.ylabel("Magnitude (dB)")
    
    plt.show()
    
    print(max(f_out))