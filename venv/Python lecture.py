#Lecture 14 Pandas - Series , Data Frame
from builtins import print

import numpy as np
import pandas as pd
from pandas import Series, DataFrame #is Arrays just like in Numpy but this time along with data Label and index.
obj = Series(['3,6,9,12'])
print(obj.values) # access values of series
print(obj.index) #access indices
#Series eg: of world war 2 casulaties
ww2_cas = Series([8700000,430000,300000,2100000,400000],index =['USSR','germany','china','japan','USA']) #defining values and indexes manually
print(ww2_cas)
#print(ww2_cas['USA'])
#check(true/False) whether countries has casulaties greater than 400000
#print(ww2_cas[ww2_cas > 400000])
#print('USSR' in ww2_cas)
ww2_dict= ww2_cas.to_dict() #converting series to dictionary
print(ww2_dict)
ww2_series = Series(ww2_dict) # passing dictionary to series
# print(ww2_series)
countries =['china','germany','japan','USA','USSR','Argentina']
obj2 = Series(ww2_dict,index = countries)
# print(obj2)
# print(pd.isnull(obj2))
# print(pd.notnull(obj2))
# print(ww2_series +obj2)
obj2.name ='worldwar 2 casulaties' # giving title to series object
# print(obj2)
obj2.index.name= 'Countries' #giving title to the index column
print(obj2)
