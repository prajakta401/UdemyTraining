#Lecture 23 Missing Data
import numpy as np
from pandas import Series,DataFrame
import pandas as pd
data = Series(['one','two','np.nan','four'])
data.isnull() # returns True is particular index is null.
data.dropna()#drops the row which has NaN values
dataframe = DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9],[np.nan,np.nan,np.nan]])
print(dataframe)# data frame with several null values
clean_dframe = dataframe.dropna()# any row with nulls will be dropped
print(clean_dframe)
x= dataframe.dropna(how= 'all')# drops  only those rows which have all the values = Nulll
print(x)
y = dataframe.dropna(axis=1)#drops the column which has one or more NaN
print(y)

npn = np.nan # create a NaN variable
dframe2 = DataFrame([[1,2,3,npn],[2,npn,5,6],[npn,7,npn,9],[1,npn,npn,npn]])# DF with many NaN
print(dframe2)
a= dframe2.dropna(thresh=3)# if we want data rows who have atleast 2 data points. Threshold
print(a)
c= dataframe.fillna(1)# fills the NaN with 1 in the dataframe ( temporary copy change)
print(c)
d= dframe2.fillna({0:'pop',1:'red',3:999})#fills column wise Nans with something else
print(d)
#permanatly filling NaN by something in a DataFrame
dframe2.fillna(0,inplace=True)
print(dframe2)

#Lecture 24 Index Hierarchy
from numpy.random import randn

ser = Series(randn(6),index=[[1,1,1,2,2,2],['a','b','c','a','b','c']])
print(ser)
print(ser.index)
#check number of levels of index
print(ser[1])
ser[:,'a']# reads all the inxes and the values who have internal index 'a'
dframe= ser.unstack()# create DF from series
print(dframe)