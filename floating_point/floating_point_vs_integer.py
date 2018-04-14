# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 23:23:56 2018

@author: Marcus
"""

import numpy as np

factor_of_two_increment = False

N = 100000

float_num = np.float32(0.0)
int_num = 0

int_inc = 1

if(factor_of_two_increment):
    float_inc = np.float32(0.0625)
else:
    float_inc = np.float32(0.01)


float_lim = float_inc * N
int_lim = N


counter = 0

while(float_num < float_lim):
    float_num += float_inc
    counter += 1
    
print('Number of iterations for a float32:', counter)
counter = 0

while(int_num < int_lim):
    int_num += int_inc
    counter += 1
    
print('Number of iterations for an integer:', counter)