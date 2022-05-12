# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:09:26 2022

@author: WESTMR
"""
from math import log,floor,ceil
from utilities import is_prime, fermat_primes, mersenne_exponents, CB_color_cycle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['axes.prop_cycle'] = matplotlib.cycler(color=CB_color_cycle) 

def all_ints_less_than(X, family=None):
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
    if family == 1 or family == None:
        for a in range(ceil(log(X/(3**2)-1,2))):
            set_of_integers.add(2**a*3**2+3**2)
    
    #Family 2
    if family == 2 or family == None:
        for a in range(ceil(log(X/3-3))):
            set_of_integers.add(2**a*3+3**2)
    
    #Family 3
    if family == 3 or family == None:
        for a in range(ceil(log(X/(3**2)-1/3))):
            set_of_integers.add(2**a*3**2+3)

    for q in [p for p in fermat_primes if p<X]:
        
        #Family 4
        if family == 4 or family == None:
            for a in range(ceil(log(X-1,2))):
                for b in range(ceil(log(X-2**a,q))):
                    set_of_integers.add(2**a+q**b)
        
        #Family 5
        if family == 5 or family == None:
            for a in range(ceil(log(X/q-1,2))):
                set_of_integers.add((2**a+1)*q)
    
    for b in [p for p in mersenne_exponents if p<log(X+1,2)]:
        
        q = 2**b-1
        
        # Family 6
        if family == 6 or family == None:
            for a in range(ceil(log((X-2)/2**b,q))):
                set_of_integers.add(q**a*2**b+2)
        
        # Family 7
        if family == 7 or family == None:
            for a in range(ceil(log((X-2**b)/2,q))):
                set_of_integers.add(2*q**a+2**b)
        
        # Family 8
        if family == 8 or family == None:
            for a in range(ceil(log(X/2**b-1,q))):
                set_of_integers.add(2**b*q**a+2**b)
            
    # Family 9
    if family == 9 or family == None:
        odd_primes = [q for q in range(3,floor((X-2)/2)) if is_prime(q)]
        for q in odd_primes:
            for a in range(ceil(log((X-2)/2,q))):
                set_of_integers.add(2*q**a+2)
            
    return set_of_integers

def ratio_of_ints_in_F_less_than(X,family=None):
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
    all_in_F = all_ints_less_than(X,family)
    return len(all_in_F)/(floor(X)-1)

def generate_plot(X_max=50000,step_size=1000,with_logs=False, individual_families=True):
    '''
    Generate and save a plot describing the proportion of integers in F.
    Figures are saved to a subdirectory named 'prop_plots/'. The filename includes
    `X_max` and `with_logs`.

    Parameters
    ----------
    X_max : int
        Upper bound on the values to consider. (default: 50000)
    step_size : int
        how often to generate a point of data for the graph (default: 1000)
    with_logs : bool
        whether or not to include the graphs of y=1/log(x) and y=1/(log(x))^2 (default: False)
    individual_families: bool
        whether or not to include graphs of proportions of integers in each of the individual families

    Returns
    -------
    None

    '''
    the_data = [(ratio_of_ints_in_F_less_than(X)) for X in range(step_size,X_max+1,step_size)]
    the_indices = [X for X in range(step_size,X_max+1,step_size)]
    X_df = pd.DataFrame(the_data, index = the_indices)
    the_legend = ["$\mathcal{F}$"]
    the_style = ["-"]
    if individual_families:
        for i in range(1,10):
            X_df[f"family {i}"] = the_data = [(ratio_of_ints_in_F_less_than(X,family=i)) for X in range(step_size,X_max+1,step_size)]
        the_legend += ["$2^a3^2+3^2$","$2^a3+3^2$","$2^a3^2+3$","$2^{a} + q^b$, $q$ Fermat",
                       "$2^aq+q$, $q$ Fermat","$q^a2^b+2$, $q=2^b-1$","$2q^a+2^b$, $q=2^b-1$",
                       "$2^b q^a+2^b$, $q=2^b-1$","$2q^a+2$, $q$ odd"]
        the_style += ['-']*9
    if with_logs:
        X_df["1/logX"] = 1/np.log(X_df.index)
        X_df["1/log^2X"] = 1/(np.log(X_df.index))**2
        the_legend += ["$1/\log X$","$1/(\log X)^2$"]
        the_style += ["--",":"]
    plot = X_df.plot(style=the_style)
    plt.title("Proportion of integers less than $X$ in a given family.")
    fig = plot.get_figure()
    ax = fig.axes[0]
    ax.set_xlabel("$X$")
    ax.set_ylabel("ratio")
    ax.legend(the_legend,loc='center left', bbox_to_anchor=(1, 0.5))
    fig.savefig(f"prop_plots/prop_in_F_up_to_{X_max}_{with_logs}_{individual_families}.pdf", bbox_inches='tight')