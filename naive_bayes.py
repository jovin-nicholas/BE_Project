# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 22:59:30 2020

@author: akshay
"""


import pandas as pd
import numpy as np
# Importing the dataset
dataset = pd.read_csv('SoftSkillData.csv')
X = dataset.iloc[:, 5:9].values
y = dataset.iloc[:, -1].values

from sklearn.preprocessing import LabelEncoder
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection  import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/10, random_state = 0)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(X_test)

from sklearn import metrics
# Model Accuracy: how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)

f = open("inputs.txt",'r')
ip = []
for i in f:
    lst = list(map(int,i.split()))
    ip.append(lst)
xip = np.array(ip).reshape(2,4)

xip = sc.transform(xip)
yip = classifier.predict(xip)
print(yip)