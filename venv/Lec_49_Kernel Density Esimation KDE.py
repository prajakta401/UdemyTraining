# LEcture # 49 Kernel Density Estimation plots KDE plt
import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats# for statistical graphs
import matplotlib as mpl#for Plotting
import matplotlib.pyplot as plt
import seaborn as sns

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