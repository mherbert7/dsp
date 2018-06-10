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

y = np.fft.ifft(X)

my_X = np.zeros(N, dtype=np.complex)
first_stage = np.zeros(N, dtype=np.complex)

#2-point DFTs
W_2 = np.array([W[0], W[0]])
a = x[0:2]
b = W_2 * x[2:4]

first_stage[0] = a[0] + b[0]
first_stage[1] = a[0] - b[0]
first_stage[2] = a[1] + b[1]
first_stage[3] = a[1] - b[1]

#4-point DFT
W_4 = np.array([W[0], W[1]])
A = first_stage[0:2]
B = W_4 * first_stage[2:4]

my_X[0] = A[0] + B[0]
my_X[1] = A[1] + B[1]
my_X[2] = A[0] - B[0]
my_X[3] = A[1] - B[1]



print(X)
print(my_X)
print(np.allclose(X, my_X))

