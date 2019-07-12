# -*- coding: utf-8 -*-
"""Logistic regression Digits datasetipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l8YnKWkS2JbZu6S_mJPetkDNuQprNKlI
"""

#In the Section we are trying to classify the digits which are in multiclass and apply data preprcessing steps 
#Build a model and finding its accuracy   

import pandas as pd
import numpy as np
from sklearn.datasets import *
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

data = load_digits() #Multiclass classification problem

X = data.data
print(X.shape)
print(X)

y =data.target
print(y.shape)
print(y)
print(np.unique(y)) #TO print the no. of unique classes

from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier

#splitting the data in to train and test in 70:30 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3) 

#Standariziing the dataset values and fitting the X_train values
scalar=StandardScaler().fit(X_train)

#Transforming the X_train and X_test calues 
X_train=scalar.transform(X_train)
X_test=scalar.transform(X_test)

from warnings import filterwarnings
filterwarnings('ignore')

#Creating Losgisitc regression model with Crossvalidation of 5 using the and find the best fit
clr = LogisticRegressionCV(multi_class='multinomial',cv=5).fit(X_train, y_train)

clr.Cs #Best C value

print(clr.score)

#Predicting the class labels
y_pre = clr.predict(X_test)   #Predicting the labels
y_pre_prob = clr.predict_proba(X_test) # Predicting the class probabilities

acc = accuracy_score(y_test, y_pre)
print(acc)

"""Summary:

We have analysed the digits dataset available at Scikitlearn.

At first step we have load the data to X and labels to Y.

Second set we have splitted the data in Xtrain, X-test, y_train and y-test
we have standarized the values of data (Xtrain and X-test)
we didn't performed any preprocessin steps due to dataset is available in 
integer form and ther are no missing values

we have performed Logisitc regressio with crossvalidation
we have found out optimum C value of 1 

we have found the accuracy of the model is >95% at the end od testing
"""

#Saving the model in file
import pickle

fle = open('Log_reg_digits_model.sav', 'wb')
pickle.dump(clr, fle)

#Loading the model from the file
model = pickle.load(open('Log_reg_digits_model.sav', 'rb'))



