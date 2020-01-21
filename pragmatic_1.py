# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 21:55:57 2020

@author: karth
"""
# Import packages and dataset
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
train=pd.read_csv(r'C:\Users\karth\karthikeyan\hackthons\dataset\train.csv')
del train['ID']
#%%
# Create independent and dependent variable
y=train.iloc[:,-1]
x=train.iloc[:,0:-1]
#%%
import matplotlib.pyplot as plt
import collections
cy=collections.Counter(y)
plt.bar(cy.keys(),cy.values())
plt.show()
#%%

#%%
# Preprocessing: Minmax scaling
# Preprocessing: Minmax scaling
ms=MinMaxScaler().fit(x)
x_scaling=ms.transform(x)
# By scaling operation score increase from 0.49045 to score=0.52721
#%%
#%%x_train,x_test,y_train,y_test=train_test_split(x_scaling,y,test_size=0.3, random_state=10)
#%%
model=XGBClassifier()
model.fit(x_scaling,y)
# score=0.52721
#%%
prediction=model.predict(x_scaling)
#%%
score=f1_score(y,prediction,average='weighted')

#%%

test=pd.read_csv(r'C:\Users\karth\karthikeyan\hackthons\dataset\test.csv')

x_t=ms.transform(test.iloc[:,1:])
#%%

prediction=model.predict(x_t)
#%%
submission=pd.DataFrame({'ID':test['ID'],'Prediction':prediction})
#%%
submission.to_csv("submission.csv",index=False)
