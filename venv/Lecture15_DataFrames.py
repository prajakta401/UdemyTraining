#Lecture 15: Data FRames
import numpy as np # array handling
import pandas as pd
from pandas import Series , DataFrame
import webbrowser # grab/scrape NFL data from website
website='http://en.wikipedia.org/wiki/NFL_win-loss_records'
webbrowser.open(website) #opens the url in nnew browser window

#copy few 10 rows and all columns on the website table on to the clipboard
nfl_frame = pd.read_clipboard() # read those 10 rows and column headers
print(nfl_frame)
print(nfl_frame.columns.values)# read column names
# print(nfl_frame.values)# read row values
print(nfl_frame.Team)# read particular column eg: "Team"
print(nfl_frame.GP)
#print(nfl_frame['First NFL Season']) # read colum whihc has multiword name
print(DataFrame(nfl_frame,columns=['Rank','Team','Won']))# fetch only specific columns.
print(DataFrame(nfl_frame,columns=['Rank','Team','Won','Stadium']))# Stadium column does not exist , but dataframe creates new column on its own.

# Retrieve rows for Data Frame

print(nfl_frame.head())# read data set)
print(nfl_frame.head(2))# read first 2 rows)
print(nfl_frame.tail()) # read last row
print(nfl_frame.tail(4)) # read last 4 rows
# nfl_frame.ix[3]# read by index  3rd index
nfl_frame['Stadium']= "Levis Stadium"
print(nfl_frame)
nfl_frame['Stadium']=np.arange(20)
print(nfl_frame)
print(len(nfl_frame.values))

#Adding series to a data Frame
stadiums = Series(["Levis Stadium","At&T stadium"],index =[19,0])#fill 19th index by LEvis and )th index by At&t
print(stadiums)
nfl_frame['Stadium']= stadiums #assign stadium series to stadium column
print(nfl_frame)
del nfl_frame['Stadium'] #delete stadium column

#add dictionary to Dataframe
data = {'City':['SF','LA','NYC'],'Population':[83,38,84]}
city_frame = DataFrame(data)
print(city_frame)

#lecture 16 Index Objects
my_ser = Series([1,2,3,4],index=['A','B','C','D'])
my_index = my_ser.index
print(my_index)


