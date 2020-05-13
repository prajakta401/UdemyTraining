#Lecture 102 SQL in Python
import sqlite3
import pandas as pd
con =sqlite3.connect("sakila.db")

#set function as our sql_to_pandas
def sql_to_df(sql_query):

#Use pandas to pass saql query using connection from SQLite
df = pd.read_sql(sql_query,con)

#show the resulting data frame
return df

#selecting multiple columns example
query = ''' SELECT first_name,last_name FROM customer; '''

#grab from first two columns
