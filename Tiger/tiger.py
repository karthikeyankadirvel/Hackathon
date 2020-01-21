# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 11:39:07 2020

@author: karth
"""

#%%
import numpy as np
import itertools
n=9

np.random.seed(seed=100)
a=[np.random.randint(1,100) for _ in range(n)]
print(a)
#%%
d=[i for i in itertools.combinations(a,3)]
#%%
trip_all=[]
trip=[]
c=0
for j in range(n):
    for i in range(j,j+n):
        i=i%n
        trip.append(a[i])
        c+=1
        if c%3==0:
            trip_all.append(trip)
            trip=[]
        
#%%    
# Sorting
for l in trip_all:
    l.sort(reverse=True)
#%%
g=n/3
s=[]
tsum=[]
c=0
triple=[]
tip=[]
for tp in trip_all:
    s.append(tp[1])
    tip.append(tp)
    c+=1
    if c%g==0:
        tsum.append(sum(s))
        triple.append(tip)
        tip=[]
        s=[]
        
#%% 

triple[tsum.index(max(tsum))]  
#%%
map()