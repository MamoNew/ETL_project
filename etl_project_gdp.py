#import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import get

page = get('https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29')


soup = BeautifulSoup(page.content, 'html.parser')

countries_table = soup.find_all(//*[@id="mw-content-text"]/div[1]/table[2]/tbody)
link=[]
for row in countries_table:
    hrefs= row.find_all('a', href=True)
    for href in hrefs:
        link.append(href['href'])

print(link)




