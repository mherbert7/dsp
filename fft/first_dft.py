# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 23:31:51 2018

@author: Marcus
"""

import numpy as np
import time

N = 2**16
samples = np.random.normal(0, 1, N) + 1j * np.random.normal(0, 1, N)

pre_calc = np.zeros(N, dtype=np.complex)
    
pre_m = np.zeros((N, N), dtype=np.complex)

for n in range(N):
    pre_calc[n] = (-1j * 2 * np.pi * n) / N
    
for m in range(N):
    pre_m[m] = np.exp(pre_calc * m)

def my_dft(x, pre_calc_vals):
    N = len(x)
    
    output = np.zeros(N, dtype=np.complex)

    for m in range(N):
        intermediate_sum = 0
        for n in range(N):
            intermediate_sum += x[n] * pre_calc_vals[m][n]
        
        output[m] = intermediate_sum
        
    return output
    
my_t0 = time.clock()
my_result = my_dft(samples, pre_m)
my_t1 = time.clock()

np_t0 = time.clock()
np_result = np.fft.fft(samples)
np_t1 = time.clock()

if(np.allclose(my_result, np_result)):
    print("Results match!")
else:
    print("Error: Results do not match!")
    
my_time = my_t1 - my_t0
np_time = np_t1 - np_t0    

print("My DFT:", my_time, "s")
print("NP DFT:", np_time, "s")

print("NP is", my_time / np_time, "times faster.")