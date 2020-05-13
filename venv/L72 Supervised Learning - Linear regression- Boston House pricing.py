#Lecture 72 ML - Supervised LEarning - Liner Regression - BOston House pricing
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from sklearn.datasets import load_boston# Sklearn is ML library

boston = load_boston()  #load the data set
# print(boston)           # this data set consists of Data Array, Target array,feature_names array and DESCR
print(boston.DESCR)
plt.hist(boston.target,bins=50)
plt.xlabel('Proces in $1000s')
plt.ylabel('Numbers of Houses')
plt.show()

#See the scatter plot for a single feature ( # rooms in house)
#RM is the lable for Number of rooms in the data set. DESCR its the 5th attribute from top(starting from zero)
plt.scatter(boston.data[:,5],boston.target)
plt.ylabel('Price in $1000s')
plt.xlabel('Numbers of rooms')
plt.show()

#Use Linear Modelling(Lmplot)  to plot similar sccatter plot but with a fit line.
boston_df = DataFrame(boston.data)          # extract Data array from the boston dataset
boston_df.columns = boston.feature_names    #extract features_names column from boston dataset
boston_df['Price'] =boston.target           #create a new column(Prices) inside Dataframe
print(boston_df.head())                     #show first few rows
print(boston_df.columns)                    #show  columns names
sns.lmplot('RM','Price',data=boston_df)     #plot Linear model graph ( x, y,data) Rooms Vs Price
plt.show()                                  #display the plot

#conclusion: Prdicted the house pricing based on Number fo rooms.
# 1) Pricing increases with increase in number of roomslinearly.
# 2) Avg pricing of the house is $20K to $25K

#Lect 73