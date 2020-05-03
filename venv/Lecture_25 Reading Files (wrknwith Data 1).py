#Lecture25 : REading and Writing Text CSV Files
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
dataframe= pd.read_csv('Lect25 CSV file reading.csv')#opens/reads the csv file
# dataframe= pd.read_csv('Lec25.csv')
print(dataframe)# prints with header row
dframe1= pd.read_csv('Lect25 CSV file reading.csv',header=None)#without header row
print(dframe1)
dframe = pd.read_table('Lect25 CSV file reading.csv',sep=',',header=None)# reading /opening a file
print(dframe)
# reading only particular number of rows instead of whole file
dframe = pd.read_table('Lect25 CSV file reading.csv',header=None,nrows=2) # reading first 2 rows only
print(dframe)

dframe.to_csv('DataFrame output.csv')#saving a dataframe output to a file
import sys# to see the output instead of saving the file
dframe.to_csv(sys.stdout,sep='_')
print(dframe)
label = [0,1,2]
# dframe.to_csv(sys.stdout,columns=[0,1,2])
# print(dframe)

#Lecture 26 Reading JSON file
# import json
# json_obj = """
# {   "zoo_animal":"Lion",
#     "food":"["Meat","Veggies","Honey"],
#     "fur":"GOlden",
#     "colths":null,
#     "diet":"zoo animals"
# }
# """
# data= json.loads(json_obj)#reading json object
# print(data)
# json.dump(data)#saving back to json file.
# dframe = DataFrame()
# dframe = DataFrame(data['diet'])#interested in reading onlt specific data from file

#Lecture27 HTML with pands
from pandas import read_html
url ='https://www.fdic.gov/bank/individual/failed/banklist.html' # read HTML data
#install beautifulsoup4 library # for scrapping sata from web
#install HTML5lib for
dframe_list =pd.read_html(url) #pd.io.html.read_html() is deprecated
htmlbank = dframe_list[0]
print(htmlbank)
print(htmlbank.values)#reads row wise data
print(htmlbank.columns.values)#reads column header


#Lecture 28 Reading Excel with pandas.
# xlsfile = pd.read_excel('Lect28 REading Excel.xlsx')
# print(xlsfile)#reads while file
# print(xlsfile.columns.values)#reads column names only
# print(xlsfile.values)#reads row data
xlsfile = pd.ExcelFile('Lect28 REading Excel.xlsx')#read the excel file name
dframe = xlsfile.parse('Sheet2')#pass the exact excel sheet name
print(dframe)








