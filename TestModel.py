# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:43:21 2021

@author: akshay
"""
import numpy as np
import dill as pickle

xip = np.array([[10,11,15,14],[20,14,18,16],[19,16,13,15]])
print("Test Data acc. skills:(Aptitude,Technical,Communication,Personality)")
print(xip)

with open('model_v1.pk' ,'rb') as f:
    loaded_model = pickle.load(f)
yip = loaded_model.predict(xip)
print("Predictions: ")
print(yip)
for i in range(len(yip)):
    ans = "Student "+str(i)+" is "
    if yip[i]==4:
        ans += "Outstanding"
    elif yip[i]==3:
        ans += "Excellent"
    elif yip[i]==2:
        ans+= "Good"
    elif yip[i]==1:
        ans+= "Average"
    elif yip[i]==0:
        ans+= "need to work hard on his Employability skills"
    print(ans)