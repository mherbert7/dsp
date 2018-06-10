# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 15:16:44 2018

@author: Marcus
"""

import numpy as np
import copy 
    
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
    
    
          x[k]    ------->      X[m] = x[k] + x[k + N/2] * (W_N)**(n)
                  \      ^
                   \    /
                    \  /(W_N)**(n)
                     \/
                     /\
                    /  \
                   /    \
                  /      v
    x[k + N/2]    ------->      X[m + N/2] = x[k] + x[k + N/2] * (W_N)**(N/2)
                 (W_N)**(n + N/2)          = x[k] - x[k + N/2] * (W_N)**(n)
               
               
    Note that the simplification on the output of the lower wing of the 
    butterfly is possible because (W_N)**(n + N/2) = -1 * (W_N)**(n). This 
    allows us to perform one less multiplication.
    
    Parameters
    ----------
    x : np.array
        An array of time-domain samples. Must only be of size 2
    W_N : np.complex128
        A phase angle factor
        
    Returns
    -------
    np.array
        An array of frequency-domain samples, being the result of a 2-point 
        DFT.
        
    Examples
    --------
    In [1]: x = np.array([0.5432 + 1.1443j, 0.9985 - 0.0114j])
    In [2]: single_butterfly(x, 1)
    Out[2]: array([ 1.5417+1.1329j, -0.4553+1.1557j])
    """

    if(len(x) != 2):
        raise ValueError("x must be only two elements long")
    
    phase_angle_multiplied = W_N * x[1]
    
    X = np.array([x[0] + phase_angle_multiplied,
                  x[0] - phase_angle_multiplied])
                  
    return X
    
def fft(x):
    """Compute a radix-2 FFT.
    
    Parameters
    ----------
    x : np.array
        An array of time-domain samples to be transformed into the frequency 
        domain.
        
    Returns
    -------
    np.array
        An array of frequency-domain samples, the output of the FFT.
        
    Raises
    ------
    ValueError
        If x is not exactly 2**n elements long, where n is a positive integer.
    """
    
    if(not((np.log2(len(x))).is_integer())):
        raise ValueError("N must be an integer power of two")
        
    #Save the size of the desired FFT
    N = len(x)
    
    #Generate the phase angle factors
    W_N_factors = generate_phase_angles(N)

    #Get the depth of the FFT (how many butterflies deep we need to go).
    fft_depth = int(np.log2(N))
    
    #Get the number of bits for a given index for an FFT of size N
    num_bits = int(np.log2(N))
    
    #Generate eversed bit indices
    indices = [(int('{:0{width}b}'.format(n, width=num_bits)[::-1], base=2),
               int('{:0{width}b}'.format(n + 1, width=num_bits)[::-1], base=2)) \
                                                            for n in range(0, N, 2)]

    f_indices = [(n, n + 1) for n in range(0, N, 2)]
    
    #Initialise the output array
    X = np.zeros(N, dtype=np.complex128)
    intermediate_results = copy.deepcopy(X)
    
    #Perform the FFT
    
    #Calculate the first level with bit-reversed indices
    for f_idcs, t_idcs in zip(f_indices, indices):
        array = np.array([x[t_idcs[0]], x[t_idcs[1]]])
        W_N = W_N_factors[0]
        
        butterfly_result = single_butterfly(array, W_N)
        
        intermediate_results[f_idcs[0]] = butterfly_result[0]
        intermediate_results[f_idcs[1]] = butterfly_result[1]
        
    X = copy.deepcopy(intermediate_results)    
    
    #Calculate further levels of the DFT
    #This is for FFTs of N > 2
    for level in range(fft_depth - 1):
        pass
            
    
    return X
    
if __name__ == "__main__":
    N = 2

    power_of_two = np.log2(N)
    
    if(not(power_of_two.is_integer())):
        raise ValueError("N must be an integer power of two")
        
    x = np.random.normal(size=N) + 1j * np.random.normal(size=N)
    
    numpy_fft = np.fft.fft(x)
    my_fft = fft(x)    
    
    print(np.allclose(numpy_fft, my_fft))