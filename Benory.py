# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:07:00 2020

@author: karth
"""

#%%
n=int(input())
#%%  
    #we will make a list of lists with just [1] in it. We will run a for loop from i= 2 to n and in each iteration
    #we will add [i]*(2i-3) in top of the list and and in bottom
    #then add i on both sides of all sub_lists
n=5   
answer=[[1]]
for i in range(2, n+1):
    t=[i]*((2*i)-1)
    print("T",t)
    answer.insert(0, t)
    answer.append(t)
#    print(answer)
#    break
    for a in answer:
        a.insert(0,i)
        a.append(i)
        print(answer)
        break
   
answerfinal=[]
#we join the elements of the string without space
for a in answer:
    answerfinal.append("".join(str(a)))
#print
#for a in answerfinal:
#    print(a)


#%%
import copy
n=5
l=[i for i in range(n-1,0,-1)]
#%%
r=2*n-(1)
answer=[]
c=0
a=[n for _ in range(r)]
answer.append(a)
#%%
c=0
ans=copy.deepcopy(a)
for i in range(len(l)):
    
    for j in range(1+c,r-c-1):
        ans[j]=l[i]
    c+=1
    
    answer.append(copy.deepcopy(ans))
for k in answer:
    print(k)
for k in range(len(answer)-2,-1,-1,):
    print(answer[k])

  
        
        
    
        
        
    
    