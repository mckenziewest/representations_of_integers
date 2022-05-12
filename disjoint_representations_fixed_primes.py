# -*- coding: utf-8 -*-
"""
Created on Thu May 12 09:09:55 2022

@author: WESTMR
"""
from utilities import is_prime
from math import log, ceil
import networkx as nx

def fix_p_q_get_all_reps(p,q,X=500):
    assert p != q
    assert is_prime(p) and is_prime(q)
    N1 = ceil(log(X-2,p))
    from collections import defaultdict
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

def fix_p_q_proportions(p,q,Y=500):
    all_reps = fix_p_q_get_all_reps(p,q,Y)
    return len(all_reps)/(Y-1)

def are_disjoint(p,q,rep1,rep2):
    vals1 = {p**rep1[0]*q**rep1[1],p**rep1[2],q**rep1[3]}
    vals2 = {p**rep2[0]*q**rep2[1],p**rep2[2],q**rep2[3]}
    return vals1.isdisjoint(vals2) 

def are_totally_disjoint(p,q,rep1,rep2):
    vals1 = {p**rep1[0]*q**rep1[1], p**rep1[2], q**rep1[3],
             p**rep1[0]*q**rep1[1]+p**rep1[2],
             p**rep1[0]*q**rep1[1]+q**rep1[3],
             p**rep1[2]+q**rep1[3]}
    vals2 = {p**rep2[0]*q**rep2[1],p**rep2[2],q**rep2[3],
             p**rep2[0]*q**rep2[1]+p**rep2[2],
             p**rep2[0]*q**rep2[1]+q**rep2[3],
             p**rep2[2]+q**rep2[3]}
    return vals1.isdisjoint(vals2) 

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

def get_max_number_disjoint_less_than(p,q,Y=500):
    all_reps = fix_p_q_get_all_reps(p,q,Y)
    num_disjoint = {X:get_max_number_disjoint(p,q,reps) for X,reps in all_reps.items()}
    n = max(num_disjoint.values())
    return n, [X for X, num in num_disjoint.items() if num == n]
    
def fix_p_q_ints_with_disjoint_less_than(p,q,Y=500):
    all_reps = fix_p_q_get_all_reps(p,q,Y)
    have_disj = {}
    for X, reps in all_reps.items():
        for r1, r2 in [(reps[i],reps[j]) for i in range(len(reps)-1) for j in range(i+1,len(reps))]:
            if are_disjoint(p,q,r1,r2):
                have_disj[X] = [r1,r2]
    the_Xs = [X for X in have_disj]
    the_Xs.sort()
    return have_disj, the_Xs
    
def fix_p_q_proportions_two_disjoint_reps(p,q,Y=500):
    all_reps = fix_p_q_get_all_reps(p,q,Y)
    return len(all_reps)/(Y-1)