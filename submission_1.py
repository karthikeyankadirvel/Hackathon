# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 21:30:14 2020

@author: karth
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 20:33:05 2020

@author: karth
"""
# Import packages and dataset
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import keras
from keras.layers import Dense,Dropout
from keras.models import Sequential
from keras.optimizers import Adam
from keras.utils import to_categorical
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
y=pd.get_dummies(y)
#%%
# Preprocessing: Minmax scaling
ms=MinMaxScaler().fit(x)
x_scaling=ms.transform(x)
# By scaling operation score increase from 0.49045 to score=0.52721


#%%
model=Sequential()
model.add(Dense(200, input_shape=(x_scaling.shape[1],)))
model.add(Dense(200))
model.add(Dropout(0.2))
model.add(Dense(150))
model.add(Dense(50))
model.add(Dense(6, activation='softmax'))
#%%

model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['acc'])

#%%

model.fit(x_scaling,y,epochs=1000)

#%%
test=pd.read_csv(r'C:\Users\karth\karthikeyan\hackthons\dataset\test.csv')
del test['ID']
x_t=ms.transform(test)
#%%
prediction=model.predict_proba(x_t)
prediction=pd.DataFrame(prediction)
#%%
prediction.columns=y.columns
submission=prediction.idxmax(axis=1)
#%%
submission.to_csv("submission.csv",index=False)