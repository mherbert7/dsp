# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 21:52:03 2018

@author: Marcus
"""

import numpy as np
import pylab as plt

#FFT Leakage Script
#If m is not an integer, then leakage will be observed

complex_in = False
plot = True

N = 64
fs = 0.53456257 * np.exp(np.pi)
ts = 1/fs
A0 = 1

t = np.linspace(0, (N - 1) * ts, N)
#t = np.arange(0, N * ts, ts) #<- This is an equivalent way to generate t

m = 37
f = m * fs / N
w = 2 * np.pi * f

if(complex_in):
    x = np.cos(w * t) + 1j*np.sin(w * t)
else:
    x = np.sin(w * t)

x *= A0

f_out = 20 * np.log10(np.abs(np.fft.fft(x)))
frequencies = np.fft.fftfreq(N, d=ts)

if(plot):
    plt.stem(f_out, markerfmt='b.')
    plt.title("FFT Output")
    plt.xlabel("Frequency index")
    plt.ylabel("Magnitude (dB)")
    
    plt.show()
    
    print(max(f_out))