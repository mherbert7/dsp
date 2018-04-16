# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 23:04:11 2018

@author: Marcus
"""

import numpy as np
import time



def my_ifft(x):
    N = len(x)
    y = np.zeros(N, dtype=np.complex)
    if (N is 1):
        return x
    else:
        Wn = np.exp(1j * 2 * np.pi / N)
        W = 1
        x_even = x[0::2]
        x_odd = x[1::2]
        y_even = my_ifft(x_even)
        y_odd = my_ifft(x_odd)
        for m in range(N//2):
            y[m] = y_even[m] + (W * y_odd[m])
            y[m + N//2] = y_even[m] - (W * y_odd[m])
            W *= Wn
        return y
        
def my_ifft_adjusted(x):
    return my_ifft(x) / len(x)
        
length = 2**14
samples = np.random.normal(0, 1, length) + 1j*np.random.normal(0, 1, length)

a0 = time.clock()
my_result = my_ifft_adjusted(samples)
a1 = time.clock()
da = a1 - a0

b0 = time.clock()
np_result = np.fft.ifft(samples)
b1 = time.clock()
db = b1 - b0

print("My IFFT took:", da, "seconds")
print("NP IFFT took:", db, "seconds")
print("NP IFFT is", da/db, "times faster")
print(np.allclose(my_result, np_result))