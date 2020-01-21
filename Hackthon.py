# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 20:33:05 2020

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
y=pd.get_dummies(y).values
#%%
# Preprocessing: Minmax scaling
x_scaling=MinMaxScaler().fit_transform(x)
# By scaling operation score increase from 0.49045 to score=0.52721
#%%
x_train,x_test,y_train,y_test=train_test_split(x_scaling,y,test_size=0.3, random_state=10)
#%%
model=XGBClassifier()
model.fit(x_train,y_train)
# score=0.52721
#%%
prediction=model.predict(x_test)
#%%
score=f1_score(y_test,prediction,average='weighted')
#score=0.52721
#%%
import keras
from keras.layers import Dense,Dropout
from keras.models import Sequential
from keras.optimizers import Adam
from keras.utils import to_categorical
#%%
model=Sequential()
model.add(Dense(200, input_shape=(x_train.shape[1],)))
model.add(Dense(200))
model.add(Dropout(0.2))
model.add(Dense(150))
model.add(Dense(50))
model.add(Dense(6, activation='softmax'))
#%%

model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['acc'])

#%%

model.fit(x_train,y_train,epochs=1000)
#%%
prediction=model.predict_classes(x_test)
#%%
y_test=[i.argmax() for i in y_test]
#%%
score=f1_score(y_test,prediction,average='weighted')
print(score)