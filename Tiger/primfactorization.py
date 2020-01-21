# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 10:45:16 2020

@author: karth
"""

#%%
n=32


#%%
# get prime number

def prim(n):
    prim=[]   
    for i in range(2,n):
        c=0
        for j in range(2,n):
            if i!=j:
                if i%j==0:
                    c+=1
                    break
        if c==0:
            prim.append(i)
    return prim
  
#%%
n=42
result=[]
l=prim(n) 
c=0
while c<len(l):
    if n%l[c]==0:
        result.append(l[c])
        n=n/l[c]
        c=-1
    c+=1
    


result      
            
            