#Lecture 50 Combining plots. Histogram + Kernel Density Estimation KDE

import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats# for statistical graphs
import matplotlib as mpl#for Plotting
import matplotlib.pyplot as plt
import seaborn as sns

dataset_A = randn(100)
sns.distplot(dataset_A,bins= 25)# overlapping Histogram and KDE graph for those random 100 poitnts
plt.show()
sns.distplot(dataset_A,bins=25,rug=True,hist=False)
plt.show()
sns.distplot(dataset_A,bins=25,
              kde_kws={'color':'indianred','label':'KDE_PLOT'},
              hist_kws={'color':'blue','label':'HIST'})# set colors
plt.show()
