# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 15:16:44 2018

@author: Marcus
"""

import numpy as np

N = 2**5

power_of_two = np.log2(N)

if(not(power_of_two.is_integer())):
    raise ValueError("N must be an integer power of two")
    
    
def generate_phase_angles(N):
    """Generate the complex phase angle factors for the FFT.
    
    We use this function to pre-calculate the phase angle factors. Although it 
    is redundant to calculate the factors for k >= N/2, this function will be 
    left simple for now, just calculating them all. It may be optimised in the 
    future, but since it will not be part of timing measurements, it doesn't 
    matter for now.
    
    Parameters
    ----------
    N : int
        The number of points in the FFT, and the number of phase angle factors 
        to calculate.
        
    Returns
    -------
    np.array
        Array of the phase angle factors.
        
    Raises
    ------
    ValueError
        If N is not an integer.
        
    Examples
    --------
    In [1]: generate_phase_angles(2)
    Out[1]: array([ 1. +0.00000000e+00j, -1. -1.22464680e-16j])
    
    In [2]: generate_phase_angles(4)
    Out[2]: 
    array([  1.00000000e+00 +0.00000000e+00j,
             6.12323400e-17 -1.00000000e+00j,
            -1.00000000e+00 -1.22464680e-16j,  
            -1.83697020e-16 +1.00000000e+00j])
    """   
    
    if(type(N) != int):
        raise ValueError("N must be an integer")
        
    W_N_factors = \
                np.array([np.exp((-1j * 2 * np.pi * k) / N) for k in range(N)])
    
    return W_N_factors

def single_butterfly(x, W_N):
    """Compute a single DFT butterfly.
    
    This is equivalent to the computation of a 2-point DFT.    
    
    This butterfly is based off a bit-reversal input FFT, as follows:
    
    x is an array of time-domain samples (the input)
    X is an array of frequency-domain samples (the output)
    
    
          x[k]    ------->      X[m] = x[k] + x[k + N/2] * (W_N)**(0)
                  \      ^
                   \    /
                    \  /(W_N)**(0)
                     \/
                     /\
                    /  \
                   /    \
                  /      v
    x[k + N/2]    ------->      X[m + N/2] = x[k] + x[k + N/2] * (W_N)**(N/2)
                  (W_N)**(N/2)             = x[k] - x[k + N/2] * (W_N)**(0)
               
               
    Note that the simplification on the output of the lower wing of the 
    butterfly is possible because (W_N)**(n + N/2) = -1 * (W_N)**(n). This 
    allows us to perform one less multiplication.
    
    Parameters
    ----------
    x : np.array
        An array of time-domain samples. Should only be of size 2
    W_N : np.complex
        A phase angle factor
        
    Returns
    -------
    np.array
        An array of frequency-domain samples, being the result of a 2-point 
        DFT.
    """
    phase_angle_multiplied = W_N * x[1]
    
    X = np.array([x[0] + phase_angle_multiplied,
                  x[0] - phase_angle_multiplied])
                  
    return X