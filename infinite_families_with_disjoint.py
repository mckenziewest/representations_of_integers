# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:09:26 2022

@author: WESTMR
"""
from math import log,floor,ceil
from utilities import is_prime, fermat_primes, mersenne_exponents
import pandas as pd
import matplotlib.pyplot as plt


import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

def all_ints_less_than(X):
    '''
    Given a positive number `X`, returns the collection of all integers
    less than X that are in one of the infinite families of integers
    that generically have two or more disjoint repesentations of the form
    $ p^aq^b + p^c + q^d $ for some primes $p$ and $q$.

    Parameters
    ----------
    X : positive number (int or float)
        Bound on integers to return.

    Returns
    -------
    set_of_integers : set
        collection of integers less than X in the infinite families.

    '''
    set_of_integers = set()
    
    # Family 1
    for a in range(ceil(log(X/(3**2)-1,2))):
        set_of_integers.add(2**a*3**2+3**2)
    
    #Family 2
    for a in range(ceil(log(X/3-3))):
        set_of_integers.add(2**a*3+3**2)
    
    #Family 3
    for a in range(ceil(log(X/(3**2)-1/3))):
        set_of_integers.add(2**a*3**2+3)

    for q in [p for p in fermat_primes if p<X]:
        
        #Family 4
        for a in range(ceil(log(X-1,2))):
            for b in range(ceil(log(X-2**a,q))):
                set_of_integers.add(2**a+q**b)
        
        #Family 5
        for a in range(ceil(log(X/q-1,2))):
            set_of_integers.add((2**a+1)*q)
    
    for b in [p for p in mersenne_exponents if p<log(X+1,2)]:
        
        q = 2**b-1
        
        # Family 6
        for a in range(ceil(log((X-2)/2**b,q))):
            set_of_integers.add(q**a*2**b+2)
        
        # Family 7
        for a in range(ceil(log((X-2**b)/2,q))):
            set_of_integers.add(2*q**a+2**b)
        
        # Family 8
        for a in range(ceil(log(X/2**b-1,q))):
            set_of_integers.add(2**b*q**a+2**b)
            
    # Family 9
    odd_primes = [q for q in range(3,floor((X-2)/2)) if is_prime(q)]
    for q in odd_primes:
        for a in range(ceil(log((X-2)/2,q))):
            set_of_integers.add(2*q**a+2)
            
    return set_of_integers

def ratio_of_ints_in_F_less_than(X):
    '''
    Computes the proportion of integers less than X that are returned by
    `all_ints_less_than(X)`.

    Parameters
    ----------
    X : positive number (int or float)
        Upper bound on the values to consider.

    Returns
    -------
    float
        Ratio of integers less than X satisfying the property.

    '''
    all_in_F = all_ints_less_than(X)
    return len(all_in_F)/(floor(X)-1)

def generate_plot(X_max=50000,step_size=1000,with_logs=True):
    the_data = [(ratio_of_ints_in_F_less_than(X),1/log(X),1/(log(X)**2)) for X in range(step_size,X_max+1,step_size)]
    the_indices = [X for X in range(step_size,X_max+1,step_size)]
    X_df = pd.DataFrame(the_data, index = the_indices)
    if with_logs:
        plot = X_df.plot(style=['-','--',':'])
        plt.legend(["Proportion of Integers in $\mathcal{F}$","$1/\log X$","$1/(\log X)^2$"])
    else:
        plot = X_df.iloc[:,0].plot(legend=False)
    fig = plot.get_figure()
    fig.savefig(f"prop_plots/prop_in_F_up_to_{X_max}_{with_logs}.pdf")
generate_plot()