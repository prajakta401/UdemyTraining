#Lecture 22 Summary Statistics
import numpy as np
import pandas as pd
import IPython
from pandas import Series, DataFrame
arr = np.array([[1,2,np.nan],[np.nan,3,4]])
dframe1 = DataFrame(arr,index=['A','B'],columns=['one','two','three'])
print(dframe1)
print(dframe1.sum()) # sums values across each column
print(dframe1.sum(axis=0)) # sums the value across each row. for Row use axis =1 , for column use axis =0
print(dframe1.min())# returns min value in column
print(dframe1.max())# returns max value in column
print(dframe1.idxmin())# returns index of the min value in column
print(dframe1.cumsum())#accumulation row wise cumulative summin across column.
print(dframe1.describe())#summary statiscs for data frame . Min , Max , ount , percentile
# from IPython.display import YouTubeVideo
# YouTubeVideo('xGbpuFNR1ME')
# YouTubeVideo('4EXNedimDMs')
from pandas_datareader import data #allow us to get some information from the web
import datetime # Library for date input
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
prices = data.get_data_yahoo(['CVX','XOM','BP'],start=datetime.datetime(2010,1,1), end=datetime.datetime(2013,1,1))['Adj Close']#get stock price at that time
print(prices.head())
# volume = data.get_data_yahoo(['CVX','XOM','BP'],start=datetime.datetime(2010,1,1), end=datetime.datetime(2013,1,1))['Volume']#get colume of stocks traded that timeframe
# print(volume.head())
# returns = prices.pct_change() #get percentage returns
# #finding correlation of stocks
# corr = returns.corr()
# # sns.heatmap(corr,annot=True)
# sns.plot
fig = plt.gcf()
plt.show()
# print(corr)
# imshow(corr)
prices.plot()


