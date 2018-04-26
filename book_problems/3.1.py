# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 22:48:24 2018

@author: Marcus
"""

import numpy as np
import pylab as plt

#3.1

N = 20
step = 1
fs = 1
m = 3.4
A0 = 1

f = (m * fs) / N
w = 2 * np.pi * f

n = np.arange(0, N, step)

x = A0 * np.sin(w * n)

X = np.abs(np.fft.fft(x))

plt.stem(n, X, markerfmt='bs')

X_lower = X[:N//2]

X_compose = np.concatenate((X_lower, X_lower[::-1]))

print(np.allclose(X_compose, X))