#Lecture 53 Heat map and Clustered Matrixes
import numpy as np
import pandas as pd
from numpy.random import randn
# from pandas import Series,DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt#plotting
import seaborn as sns#
from scipy import stats# for stats

flight_dframe = sns.load_dataset('flights')#loding the data set availbale in sns library
print(flight_dframe.head())
flight_dframe = flight_dframe.pivot('month','year','passengers')
print(flight_dframe)
sns.heatmap(flight_dframe,cmap="Greens",annot=True,fmt='d')
plt.show()
sns.heatmap(flight_dframe,center=flight_dframe.loc['January',1955])# 2 color gradients split at center
plt.show()

#drawing multiple plots in one window figure  "Subplots
fig,(axis1,axis2) = plt.subplots(2,1)#figure name , 2 sets of axis ( 2rows and 1 colun
yearly_flights = flight_dframe.sum()#sum of flights for each year
print(yearly_flights)
years = pd.Series(yearly_flights.index.values)
years = pd.DataFrame(years)
flights = pd.Series(yearly_flights.values)
flights = pd.DataFrame(flights)
year_dframe = pd.concat((years,flights),axis = 1)
year_dframe.columns =['Year','Flights']
sns.barplot('Year',y='Flights',data=year_dframe,ax=axis1,color='Blue')
sns.heatmap(flight_dframe,cmap='Blues',ax=axis2,cbar_kws={'orientation':'horizontal'})
plt.show()
#drawing cluster map. Similar data is next to each other
sns.clustermap(flight_dframe)#similar rows are next to eachother
plt.show()
