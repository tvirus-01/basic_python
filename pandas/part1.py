# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:52:09 2019

@author: adnan
"""


import pandas as pd
import numpy as np

#one-dimensional dataset
data = [1,2,3,4,5,6]
df1 = pd.DataFrame(data)
df1

#two-dimensinal dataset
dictonary = {'fruits':['apple','mango','grape'],'count':['23','154','1000']}
df2 = pd.DataFrame(dictonary)
df2

#convert one-dimensional dataset into two-dimnesional
series = pd.Series([6,12,18], index=['a', 'b','c'])
df3 = pd.DataFrame(series)
df3

#create dataframe using numpy array
nparray = np.array([['5000','6875','5820','4729'],['jhon','mokles','kuddus','jack']])
df4 = pd.DataFrame({'name':nparray[1],'sellary':nparray[0]})
df4
