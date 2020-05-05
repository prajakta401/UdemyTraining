##Lecture 31 Concatenate : join DF and Matrices together
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
# arr1 = np.arange(9).reshape(3,3)
# print(arr1)
# #concatenate 2 arrays in Numpy
# print(np.concatenate([arr1,arr1],axis =1))#side by side copies
#
# print(np.concatenate([arr1,arr1],axis =0))# top of eachother copy
# #Concatenating 2 DataFrames in PAndas
# ser1 = Series([0,1,2],index=['T','U','V'])
# print(ser1)
# ser2 = Series([3,4],index=['X','Y'])
# print(ser2)
# print(pd.concat([ser1,ser2]))#top of each other
# print(pd.concat([ser1,ser2],axis=1))#concate along Y axis top of each other. BAsically creates a Data Frame
# print(pd.concat([ser1,ser2],keys=['cat1','cat2']))#gives a label to index (hirachichal indexing)
#
# #cancatenate two DataFrames's
# dframe1 = DataFrame(np.random.rand(4,3),columns=['X','Y','Z'])
# dframe2 = DataFrame(np.random.rand(3,3),columns=['Y','Q','X'])
# y= pd.concat([dframe1,dframe2])#2 DF are conctaednated with their respective index
# print(y)
# z = pd.concat([dframe1,dframe2],ignore_index=True)#2 DF are conctaednated with continiuous index 0 ,1 ,2...10
# print(z)
#
# #Lecture 32 Combining Dataframes with overlapping indexis
#
# #Combining two series : ser1.combine_first(ser2)
# ser1 = Series([2,np.nan,4,np.nan,6,np.nan],index=['Q','R','S','T','U','V'])
# print(ser1)
# ser2 = Series(np.arange(len(ser1)),dtype=np.float64,index=['Q','R','S','T','U','V'])
# print(ser2)
# #logical WHERE condition
# Series(np.where(pd.isnull(ser1),ser2,ser1),index=ser1.index)#for every null values in Ser1 , replace by value of Ser2 , else set ser1 vales.
# ser1.combine_first(ser2)#for every null values in Ser1 , replace by value of Ser2 , else set ser1 vales.
#
# #combining two DataFrames
# nan = np.nan
# dframe_odd = DataFrame({'X':[1,nan,3,nan],'Y':[nan,5,nan,7],'Z':[nan,9,nan,11]})
# print(dframe_odd)
# dframe_even = DataFrame({'X':[2,4,nan,6,8],'Y':[nan,10,12,14,16]})
# print(dframe_even)
# print(dframe_odd.combine_first(dframe_even))

#Lecture 33 Reshaping
#Datframe reshaping using Stack, Unstack()
# dframe1 = DataFrame(np.arange(8).reshape(2,4),index=pd.Index(['LA','SF'],name='city'),
#                     columns= pd.Index(['A','B','C','D'],name='letter'))
# print(dframe1)
# dframe_st =dframe1.stack()#pivot it by CIty , Letter
# print(dframe_st)
# M =dframe_st.unstack()
# print(M)# converst eh pivot back to DataFrame
# print(dframe_st.unstack('city')) #Pivot by city. City becoms column header . ABCD become rows
#
# # REshaping Series using stack, unstcak()
# ser1 = Series([0,1,2],index=['Q','X','Y'])
# ser2 = Series([4,5,6],index=['X','Y','Z'])
# print(ser1)
# print(ser2)
#
# dframe = pd.concat([ser2,ser2],keys=['Alpha','Beta'])#concatenateed two series
# print(dframe)
# x= dframe.unstack()#make series into DataFrame with Nans in it
# print(x)
# y= dframe.unstack().stack()#Nans ar gone
# print(y)
# dframe =dframe.unstack()
# z= dframe.stack(dropna=False)
# print(z)
#
# #Lecture34 PIVOTING. Pivot Function does not support data aggrigation(sum/count)
# xlsfile = pd.ExcelFile('Candidate report.xlsx')
# candidate_data = xlsfile.parse('Sheet1')
# print(candidate_data)
# pivot_data = candidate_data.pivot('state','Quarter','CandidateID')# shows the Candidate # as is in the picot.
# print(pivot_data)
#
# #Lecture25 Duplicated in DataFrmaes
# dframe = DataFrame({'key1':['A']*2 + ['B']*3,
#                    'key2':[2,2,2,3,3]})
# print(dframe)
# print(dframe.duplicated())#true/false gives if a row is duplicate in DF.
# print(dframe.drop_duplicates())#get rid of duplicates from top
# print(dframe.drop_duplicates(['key1']))# gets rid of duplicated in sepcific columns fro top
# print(dframe.drop_duplicates(['key1'],keep= 'last')) #gets rid of duplicated in sepcific columns from bottom

#Lecture36 MApping. Adding column to DF

# dframe = DataFrame({'city':['Alma','Brian Head','Fox Park'],'Altitude':[3158,3000,2456]})
# print(dframe)
# state_map ={'Alma':'Colorado','Brian Head':'Utah','Fox Park':'Wyoming'}#dictinary
# dframe['state']=dframe['city'].map(state_map)#adding state column (Vlookup)
# print(dframe)

#Lecture 37 REplace
# ser1 = Series([1,2,3,4,1,2,3,4])
# print(ser1)
# x= ser1.replace(1,np.nan)# replaces 1 , bu NaN
# print(x)
# z= ser1.replace([1,4],[100,400])#replacing multiple values at once
# print(z)

#Lecture 38 REnaming Indexes
# dframe = DataFrame(np.arange(12).reshape(3,4),index=['NY','LA','SF'],
#                    columns=['A','B','C','D'])
# print(dframe)
# # dframe.index = dframe.index.map(str.lower)#convert to lower case initials
# # print(dframe)
# print(dframe.rename(index=str.title,columns=str.lower))
#
# #Lecture 39 Binning
# years =[1969,1987,1990,1991,1992,1998,2008,2008,2012,2013,2015]
# decade_bins=[1960,1970,1980,1990,2000,2010,2020]
# decade_cat = pd.cut(years,decade_bins)
# print(decade_cat)
# print(pd.cut(years,2,precision=1))# divides years list into 2 categorues.
# print(decade_cat.categories)
# print(pd.value_counts(decade_cat))# give us how many years were there in that particular decade categry

#Lecture 40 Outliers
# np.random.seed(12345)
# dframe = DataFrame(np.random.randn(1000,4))
# print(dframe.head())
# print(dframe.tail())
# print(dframe.describe())
# col = dframe[0]
# print(col.head())
# print(col[np.abs(col)>3])#print all the values which are >3 in that column
# print(dframe[(np.abs(dframe)>3).any(1)])# returs eevry row in DF which had abs value > 3
# dframe[np.abs(dframe)>3] = np.sign(dframe)*3# any value in DF where abs > 3  , set it as 3 or -3
# print(dframe.describe())


#Lecture 41 Permutation - Reordering

dframe = DataFrame(np.arange(16).reshape(4,4))
print(dframe)
blender = np.random.permutation(4)# from a random 4 digit number using ( 0,1,2,3)
print(blender)
print(dframe.take(blender))# reorders the original DF  as per blender number sequence
box = np.array([1,2,3])
shaker = np.random.randint(0,len(box),size=10)# create a random array of size 10 using digits (0,1,2,3)
print(shaker)
hand_grab = box.take(shaker)
print(hand_grab)