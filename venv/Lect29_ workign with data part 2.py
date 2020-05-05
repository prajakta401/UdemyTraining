#Lecture 29 - Merge
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
dframe= DataFrame({'key':['X','Z','Y','Z','X','X'],'data_set1':np.arange(6)})
# print(dframe)
dframe2= DataFrame({'key':['Q','Y','Z'],'data_set2':[1,2,3]})
# print(dframe2)
# print(pd.merge(dframe,dframe2))# 1 is to many. 1st element of DF1 is manpped and checked against all the values in dataset2
# print(pd.merge(dframe,dframe2,on='key'))#merging based on specifc column
# print(pd.merge(dframe,dframe2,on='key',how='left'))# left join
# print(pd.merge(dframe,dframe2,on='key',how='right'))#right join
# print(pd.merge(dframe,dframe2,on='key',how='outer'))#union of two dat Frames
# #Many to Many

# dframe3= DataFrame({'Key':['X','X','X','Y','Z','Z'],'data_set_3':range(6)})
# print(dframe3)
# dframe4= DataFrame({'Key':['Y','Y','X','X','Z'],'data_set_4':range(5)})
# print(dframe4)
# print(pd.merge(dframe3,dframe4))
#
# dfleft = DataFrame({'Key1':['SF','SF','LA'],'key2':['one','two','three'],'left_data':[10,20,30]})
# print(dfleft)
# dfright = DataFrame({'Key1':['SF','SF','LA','LA'],'key2':['one','one','one','two'],'right_data':[40,50,60,70]})
# print(dfright)
# print(pd.merge(dfleft,dfright,on=['Key1','key2'],how='outer'))

#Lecture 30 Merging on Index
df_left = DataFrame({'Key':['x','y','z','x','y'],'data':range(5)})
# print(df_left)
df_right = DataFrame({'group_data':[10,20]},index=['x','y'])
# print(df_right)
# print(pd.merge(df_left,df_right,left_on='Key',right_index=True))
#hirarchly reindexing
df_left_hr = DataFrame({'key1':['SF','SF','SF','LA','LA'],
                        'key2':[10,20,30,20,30],
                        'dataset':np.arange(5)})
print(df_left_hr)
df_right_hr = DataFrame(np.arange(10).reshape(5,2),
                        index=[['LA','LA','SF','SF','SF'],
                               [20,10,20,10,20]],
                        columns=['col1','col2'])
print(df_right_hr)
pd.merge(df_left_hr,df_right_hr,left_on=['key1','key2'],right_index=True)
x= df_left.join(df_right)
print(x)

