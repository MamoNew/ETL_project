import pandas as pd
import numpy as np
import sqlite3
import datetime
from bs4 import BeautifulSoup
import requests
# Code for ETL operations on Country-GDP data
def extract(url, table_attribs):
    url ='https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
    page = requests.get(url).text
    data = BeautifulSoup(page,'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('tbody')
    rows = tables[2].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col)!=0:
            if col[0].find('a') is not None and '—' not in col[2]:
                data_dict = {"Country": col[0].a.contents[0],
                             "GDP_USD_millions": col[2].contents[0]}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
    return df

def transform(df):
    GDP_list=df["GDP_USD_millions"].tolist()
    GDP_list= [float("".join(x.split(','))) for x in GDP_list]
    GDP_list= [np.round(x/1000,2) for x in GDP_list]
    
  




