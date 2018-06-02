# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 23:33:19 2018

@author: Marcus
"""

import numpy as np

def generate_W_N_table(N):
    """Generate a table of phase angles.
    
    Parameters
    ----------
    N : int
        The number of phase angles needed. Must be a power of 2.
        
    Returns
    -------
    np.array
        An array of the phase angles.
    """
    if((N % 2) != 0):
        raise ValueError("N must be a power of 2")
    
    elif(N <= 0):
        raise ValueError("N must be a positive integer")
    
    W_N = np.zeros(N, dtype=np.complex)
    
    W = np.exp(-1j * 2 * np.pi / N)
    
    for idx in range(N//2):
        W_N[idx] = np.power(W, idx)
    
    W_N[N//2:] = -1 * W_N[:N//2]
    
    return W_N
    
N = 4

x = np.random.normal(size=N)

W = generate_W_N_table(N)

X = np.fft.fft(x)

my_X = np.zeros(N, dtype=np.complex)
first_stage = np.zeros(N, dtype=np.complex)

first_stage[0] = x[0] + W[0] * x[2]
first_stage[1] = x[0] + W[2] * x[2]
first_stage[2] = x[1] + W[0] * x[3]
first_stage[3] = x[1] + W[2] * x[3]


my_X[0] = first_stage[0] + W[0] * first_stage[2]
my_X[1] = first_stage[1] + W[1] * first_stage[3]
my_X[2] = W[2] * first_stage[2] + first_stage[0]
my_X[3] = W[3] * first_stage[3] + first_stage[1]



print(X)
print(my_X)
print(np.allclose(X, my_X))

