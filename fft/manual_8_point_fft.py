# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 03:24:34 2018

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
    
N = 8

x = np.random.normal(size=N)

W = generate_W_N_table(N)

X = np.fft.fft(x)

second_stage = np.zeros(N, dtype=np.complex)
first_stage = np.zeros(N, dtype=np.complex)
X_fft = np.zeros(N, dtype=np.complex)

#2-point DFTs
W_2 = np.array([W[0], W[0], W[0], W[0]])
l = x[0:4]
u = W_2 * x[4:8]

first_stage[0] = l[0] + u[0]
first_stage[1] = l[0] - u[0]
first_stage[2] = l[1] + u[1]
first_stage[3] = l[1] - u[1]

first_stage[4] = l[2] + u[2]
first_stage[5] = l[2] - u[2]
first_stage[6] = l[3] + u[3]
first_stage[7] = l[3] - u[3]

#4-point DFTs
W_4 = np.array([W[0], W[2], W[0], W[2]])
L = first_stage[0:4]
U = W_4 * first_stage[4:8]

second_stage[0] = L[0] + U[0]
second_stage[1] = L[1] + U[1]
second_stage[2] = L[0] - U[0]
second_stage[3] = L[1] - U[1]

second_stage[4] = L[2] + U[2]
second_stage[5] = L[3] + U[3]
second_stage[6] = L[2] - U[2]
second_stage[7] = L[3] - U[3]

#8-point DFT
W_8 = np.array([W[0], W[1], W[2], W[3]])
LX = second_stage[0:4]
UX = W_8 * second_stage[4:8]

X_fft[0] = LX[0] + UX[0]
X_fft[1] = LX[1] + UX[1]
X_fft[2] = LX[2] + UX[2]
X_fft[3] = LX[3] + UX[3]
X_fft[4] = LX[0] - UX[0]
X_fft[5] = LX[1] - UX[1]
X_fft[6] = LX[2] - UX[2]
X_fft[7] = LX[3] - UX[3]


print(X)
print(X_fft)
print(np.allclose(X, X_fft))

