# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:10:05 2022

@author: WESTMR
"""
# Import Statements

from math import sqrt



def is_prime(p):
    '''
    returns `True` if `p` is prime and `False` otherwise.
    '''
    for a in range(2,int(sqrt(p))+1):
        if p%a == 0:
            return False
    return True


fermat_primes = [3, 5, 17, 257, 65537]
mersenne_exponents = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607,
                   1279, 2203, 2281,3217, 4253, 4423, 9689, 9941, 11213,
                   19937, 21701, 23209, 44497, 86243,110503, 132049, 216091, 
                   756839,859433, 1257787, 1398269, 2976221, 3021377, 6972593, 
                   13466917, 20996011, 24036583, 25964951, 30402457, 32582657, 
                   37156667, 42643801, 43112609, 57885161,74207281, 77232917, 
                   82589933]

# Colorblind cycle published by @thriveth on GitHub
# https://gist.github.com/thriveth/8560036
CB_color_cycle = ['black','#377eb8', '#ff7f00', '#4daf4a',
                  '#f781bf', '#a65628', '#984ea3',
                  '#999999', '#e41a1c', '#dede00','gray','gray']