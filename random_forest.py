# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:57:49 2020

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
labelencoder_kt = LabelEncoder()
X[:,1] = labelencoder_kt.fit_transform(X[:,1])

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection  import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/10, random_state = 0)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Import the model we are using
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=1000, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

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