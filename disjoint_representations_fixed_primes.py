# -*- coding: utf-8 -*-
"""
Created on Thu May 12 09:09:55 2022

@author: WESTMR
"""
from utilities import is_prime
from math import log, ceil
from collections import defaultdict
import networkx as nx

def fix_p_q_get_all_reps(p,q,X=500):
    assert p != q
    assert is_prime(p) and is_prime(q)
    N1 = ceil(log(X-2,p))
    reps = defaultdict(list)
    for alpha in range(N1):
        M1 = ceil(log((X-2)/(p**alpha),q))
        for beta in range(M1):
            N2 = ceil(log(X-1-p**alpha*q**beta,p))
            for gamma in range(N2):
                M2 = ceil(log(X-p**gamma-p**alpha*q**beta,q))
                for delta in range(M2):
                    x = p**alpha*q**beta + p**gamma + q**delta
                    if x < X:
                        reps[x].append([alpha,beta,gamma,delta])
    return reps

def fix_p_q_proportions(p,q,X=500):
    all_reps = fix_p_q_get_all_reps(p,q,X)
    return len(all_reps)/(X-1)

def are_disjoint(p,q,rep1,rep2):
    terms1 = {p**rep1[0]*q**rep1[1],p**rep1[2],q**rep1[3]}
    terms2 = {p**rep2[0]*q**rep2[1],p**rep2[2],q**rep2[3]}
    return terms1.isdisjoint(terms2) 

def are_totally_disjoint(p,q,rep1,rep2):
    subsums = [{p**rep[0]*q**rep[1], p**rep[2], q**rep[3],
                p**rep[0]*q**rep[1]+p**rep[2],
                p**rep[0]*q**rep[1]+q**rep[3],
                p**rep[2]+q**rep[3]}
               for rep in (rep1,rep2)]
    return subsums[0].isdisjoint(subsums[1]) 

def get_max_disjoint_set(p,q,reps):
    G = nx.Graph()
    G.add_nodes_from([i for i in range(len(reps))])
    G.add_edges_from([(i,j) for i in range(len(reps)) for j in range(len(reps))
                          if are_disjoint(p,q,reps[i],reps[j])])
    disj_tuples = [C for C in nx.find_cliques(G)]
    max_set_size = max(len(C) for C in disj_tuples)
    return [[reps[i] for i in C] for C in disj_tuples if len(C) == max_set_size]

def get_max_number_disjoint(p,q,reps):
    return(len(get_max_disjoint_set(p,q,reps)[0]))

def get_max_number_disjoint_less_than(p,q,X=500):
    all_reps = fix_p_q_get_all_reps(p,q,X)
    num_disjoint = {x: get_max_number_disjoint(p,q,reps) for x,reps in all_reps.items()}
    n = max(num_disjoint.values())
    return n, [x for x, num in num_disjoint.items() if num == n]
    
def fix_p_q_ints_with_disjoint_less_than(p,q,X=500):
    all_reps = fix_p_q_get_all_reps(p,q,X)
    have_disj = defaultdict(list)
    for x, reps in all_reps.items():
        for r1, r2 in [(reps[i],reps[j]) for i in range(len(reps)-1) for j in range(i+1,len(reps))]:
            if are_disjoint(p,q,r1,r2):
                have_disj[x].append([r1,r2])
    the_xs = [x for x in have_disj]
    the_xs.sort()
    return have_disj, the_xs
    
def fix_p_q_proportions_two_disjoint_reps(p,q,X=500):
    have_disj, the_xs = fix_p_q_ints_with_disjoint_less_than(p,q,X)
    return len(the_xs)/(X-1)


def get_largest_int_with_disjoint_representations(p,q,X=500):
    representation_dictionary = fix_p_q_ints_with_disjoint_less_than(p, q,X)[0]
    the_keys = [k for k in representation_dictionary.keys()]
    the_biggest = max(the_keys)
    representations = [f"${p}^{{{r[0]}}}{q}^{{{r[1]}}}+{p}^{{{r[2]}}}+{q}^{{{r[3]}}}$" for r in representation_dictionary[the_biggest][0]]
    return the_biggest, representations,len(the_keys)
    
def fix_p_q_ints_with_totally_disjoint_less_than(p,q,X=500):
    all_reps = fix_p_q_get_all_reps(p,q,X)
    have_disj = defaultdict(list)
    for x, reps in all_reps.items():
        for r1, r2 in [(reps[i],reps[j]) for i in range(len(reps)-1) for j in range(i+1,len(reps))]:
            if are_totally_disjoint(p,q,r1,r2):
                have_disj[x].append([r1,r2])
    the_xs = [x for x in have_disj]
    the_xs.sort()
    return have_disj, the_xs


def get_largest_int_with_totally_disjoint_representations(p,q,X=500):
    representation_dictionary = fix_p_q_ints_with_disjoint_less_than(p, q,X)[0]
    the_keys = [k for k in representation_dictionary.keys()]
    if len(the_keys) > 0:
        the_biggest = max(the_keys)
        reps = representation_dictionary[the_biggest][0]
    else:
        the_biggest = 0
        reps = []
    return the_biggest, reps,len(the_keys)

def make_table_odd_primes_disjoint(X = 1000000000,largest_prime = 19):
    table = ""
    for p,q in [(p,q) for p in range(3,largest_prime) for q in range(p+1,largest_prime+1) if is_prime(p) and is_prime(q)]:
        big, reps, number = get_largest_int_with_totally_disjoint_representations(p, q,X)
        representations = "=".join([f"{p}^{{{r[0]}}}{q}^{{{r[1]}}}+{p}^{{{r[2]}}}+{q}^{{{r[3]}}}" for r in reps if len(r)==4])
        table += f"{p}&{q}&{number:,}&{big:,}&${representations}$\\\\\n"
    print(table)