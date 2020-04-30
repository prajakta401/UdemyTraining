
#Lecture 17 REindexing
import numpy as np #Library
from numpy.random import randn #Random is Module . Randn is method
import pandas as pd
from pandas import Series , DataFrame

ser1 = Series([1,2,3,4],index=['A','B','C','D'])
ser2 = ser1.reindex(['A','B','C','D','E','F'])
print(ser2)
x=ser2.reindex(['A','B','C','D','E','F','G'],fill_value=0) # this fills G = 0
print(x)

# ser3 = Series(['USA','Mexico','Canada'],index=[0,5,10])
# print(ser3)
# ranger = range(15)# makes range of 15 point. ( 0..14)
# print(ranger)
# ser3.reindex(ranger,method='ffill') # it will forward fill 0 to 4 will be USA
# #ser3.reindex_like(ranger,method='ffill')
# print(ser3)

dframe = DataFrame(randn(25).reshape((5,5)),index=['A','B','D','E','F'],columns=['col1','col2','col3','col4','col5']) #'
print(dframe)
dframe2 = dframe.reindex(['A','B','C','D','E','F']) # fills C row with NaN
print(dframe2)
new_columns = ['col1','col2','col3','col4','col5','col6']#explicitly reindexing columns
dframe3 =dframe2.reindex(columns= new_columns) # column 6 should get added with NN rows content
print(dframe3)

# #Reindexing using .ix #had same issue with pandas 1.0.0, this worked for me
# # Open Anaconda Prompt (cmd) as Administrator, then
#  conda install pandas==0.25.1

# Your newer pandas version will be overwritten by older one!
# df2= dframe.ix[['A','B','C','D','E','F'],new_columns]
# print(df2)

#Lecture 18  Drop Entries
ser1 = Series(np.arange(3),index=['a','b','c'])
print(ser1)
ser2 =ser1.drop('b') # Drops B row from the series
print(ser2)

dframe1 = DataFrame(np.arange(9).reshape((3,3)),index= ['SF','LA','NY'],columns=['pop','size','year'])
print(dframe1)
x= dframe1.drop('LA') #drop LA reow from dataframe
print(x)
print(dframe1)
print(dframe1.drop('year',axis=1)) #drops year column from data frame.
print(dframe1)

#LEcture 19 Selecting Entries in Series and DataFrames
ser1 = Series(np.arange(3),index=['A','B','C'])
ser1 = 2*ser1
print(ser1)
x= ser1['B'] #read values of B which is 2
print(x)
x= ser1[['A','B']] #read values of A, B which is 0,2
print(x)
x= ser1[ser1>3]#read values of all the indices which are greater than 3.. so it reads inxed  C  4
print(x)
x= ser1[ser1>3] =10# replace and set any value which is greater than 3 to 10. so C= 10
print(x)

# Selecting form DataFrames
dframe = DataFrame(np.arange(25).reshape((5,5)),index= ['LA','NYC','SF','DC','Chi'], columns=['A','B','C','D','E'])
print(dframe)
x= dframe['B'] # reading B column
print(x)
x=dframe[['A','B','E']] #reading multiple columns A B C
print(x)
x= dframe[dframe['C']>8] # reads the frame /rows >8.
print(x)
x= dframe > 10 # returns True if values in each cell is >10 else False
print(x)
# x= dframe.ix['LA'] #conda install pandas==0.25.1
# print(x)

#Lecture 20 Data Allignment
