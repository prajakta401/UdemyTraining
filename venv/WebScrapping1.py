#Lect 105 WebScrapping - Part 1 ( extracting data from website)
import pandas as pd
from bs4 import BeautifulSoup# pulling data out of HTML and XML files. scrapping/searching data from websites
import requests             # HTML requests GET , POST
from pandas import Series,DataFrame

#Scrape Legislative reports from the Univ of California
url ='https://www.ucop.edu/operating-budget/budgets-and-reports/legislative-reports/2013-14-legislative-session.html'

#setting up request to grab the content from Web
result = requests.get(url)  # sending get request and saving the response as response object
c = result.content          # content/data from website
soup = BeautifulSoup(c,features="lxml")     #search for what we want in that request (result content)

#Now we need to find the class and ID names from the HTML code. go to website and check the HTML code by rightclick
summary = soup.find('div',{'class':'list-land','id':'content'}) #pass dictionary for class and ID
tables = soup.find_all('table')

# #Part 2 redinnd and converting website content into Dataframe.
data =[]
rows = tables[0].find_all('tr')   # find every row in that HTML table
for tr in rows:                 #for every item in that row
    cols = tr.find_all('td')    #find every column in tha row
    for td in cols:             #in that every column
        text = td.find(text=True)#fidn if there is any text there?
        # print(text)             # if yes then print that text
        data.append(text)       #append to the Data Frame

# print(data)
reports = []
date = []
index=0

for item in data:
    if 'pdf' in item:#check if there is pdf file
        date.append(data[index-1])# if yes then ,read the previous row(-1) which is Date row. and append the date oin date column

        reports.append(item.replace(u'\xa0',u' '))#append the report name in the REport column. but also replace those weird non unicode objects /characters by space

    index +=1

date1 = Series(date)
# print(date1)
reports1 = Series(reports)
# print(reports1)
legislative_df = pd.concat([date1,reports1])
legislative_df.columns =['Date','Report']
print(legislative_df)
