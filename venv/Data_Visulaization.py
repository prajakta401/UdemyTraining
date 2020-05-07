#Data Viaulization
#Lecture 47 Installing Seaborn - Statistical librairy for Data Visualization
#Histogram
import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats# for statistical graphs
import matplotlib as mpl#for Plotting
import matplotlib.pyplot as plt
import seaborn as sns

dataset1 = randn(100)#random normal distribution dataset
plt.hist(dataset1)#draw histogram
plt.show()#display the graph

dataset2 = randn(80)
plt.hist(dataset2,color='indianred')
# plt.show()
plt.hist(dataset1,density= True,color='indianred',alpha=0.5,bins=20)
plt.hist(dataset2,density= True,alpha=0.5,bins=20)
# plt.show()


data1 = randn(1000)
data2 = randn(1000)
sns.jointplot(data1,data2)#joint distribution
# plt.show()
sns.jointplot(data1,data2,kind='hex')#hex bin  eg: color pallet honeycomb
# plt.show()

# LEcture # 49 Kernel Density Estimation plots KDE plt
dataset = randn(25)
# sns.rugplot(dataset)
# plt.ylim(0,1)
# plt.hist(dataset,alpha=0.3)
# # sns.rugplot((dataset))
# # # plt.show()
sns.kdeplot(dataset)# frequency wave
plt.show()
sns.kdeplot(dataset,cumulative=True)


#Lecture 50 Combining plots. Histogram + Kernel Density Estimation KDE
dataset_A = randn(100)
sns.distplot(dataset_A,bins= 25)


