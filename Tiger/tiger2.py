# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:17:43 2020

@author: karth
"""

n=5
import numpy as np
import math
n=9

np.random.seed(seed=100)
a=[np.random.randint(1,100) for _ in range(n)]
#%%
a=[1,2,3,4,5]
n=5
n_number=[]
for i in range(n-1):
    minium=min(a[i],a[i+1])
    if minium%2==0:
        minium=0
    t=math.floor(minium/2)
    print(t)
    n_number.append(t)
print(sum(n_number))

#%%

n=input("Enter numbers").strip().split()


