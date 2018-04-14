# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 23:23:07 2018

@author: Marcus
"""

import numpy as np
import time

def my_fft(x):
    N = len(x)
    y = np.zeros(N, dtype=np.complex)
    if (N is 1):
        return x
    else:
        Wn = np.exp(-1j * 2 * np.pi / N)
        W = 1
        x_even = x[0::2]
        x_odd = x[1::2]
        y_even = my_fft(x_even)
        y_odd = my_fft(x_odd)
        for m in range(N//2):
            y[m] = y_even[m] + (W * y_odd[m])
            y[m + N//2] = y_even[m] - (W * y_odd[m])
            W *= Wn
        return y
        
length = 2**16
samples = np.random.normal(0, 1, length) + 1j*np.random.normal(0, 1, length)

a0 = time.clock()
my_result = my_fft(samples)
a1 = time.clock()
da = a1 - a0

b0 = time.clock()
np_result = np.fft.fft(samples)
b1 = time.clock()
db = b1 - b0

print("My FFT took:", da, "seconds")
print("NP FFT took:", db, "seconds")
print("NP FFT is", da/db, "times faster")
print(np.allclose(my_result, np_result))