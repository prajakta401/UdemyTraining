#Lecture20 Data Allignment
#Adding two Series
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
ser1 = Series([0,1,2],index=['A','B','C'])
print(ser1)
ser2 = Series ([3,4,5,6],index =['A','B','C','D'])
print(ser2)
ser3= ser1 +ser2 # pandas added up values were indexes match, and NaN where index doesnt match
print(ser3)

#adding two Data Frame
dataframe1 = DataFrame(np.arange(4).reshape((2,2)),columns=list('AB'), index=['NYC','LA'])
dataframe2 = DataFrame(np.arange(9).reshape((3,3)),columns=list('ADC'), index=['NYC','SF','LA'])
dataframe3= dataframe1 + dataframe2
print(dataframe3)
#replacing NaN values with 0
x = dataframe1.add(dataframe2,fill_value=0)
print(x)
print(dataframe2)

# ser3 = dataframe3.ix[0]
# print(ser3)

#Lecture 21 Rank and Sort
ser1 = Series([4,7,2,9,66,43,99,34])
# x= ser1.sort_index() # sort in ascending by index
# prin
# t(x)
# print(ser1.sort_values(ascending= True))#order by asc values
# print(ser1.sort_values(ascending= False))#order by desc values
# print(ser1.sort_index(ascending= False))#order by desc index
# print(ser1.sort_index(ascending= True))#order by asc index
ser1 = Series([4,7,2,99,34],index=['A','C','D','E','B'])
print(ser1.sort_index(ascending= False))#order by desc index
print(ser1.sort_values(ascending= True))#order by asc values
# print(ser1.order)#order is obselete method
from numpy.random import randn
ser2 = Series(randn(10))
print(ser2)
print(ser2.sort_values(ascending= True))#order by asc values