import csv

import requests
from bs4 import BeautifulSoup
import html5lib
URL = "http://www.values.com/inspirational-quotes"
resp = requests.get(URL)
#print(resp.content)
soup = BeautifulSoup(resp.content,"html5lib")
#print(soup.prettify())
table = soup.find('div',attrs={'id':"all_quotes"})
#print(table.prettify())
quotes = []
for row in table.findAll('div',attrs={'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(' #')[0]
    quote['author'] = row.img['alt'].split(' #')[1]
    quotes.append(quote)
filename = "inspirational_quotes.csv"
with open(filename,'w',newline='') as file:
    csvobj = csv.DictWriter(file,['theme','url','img','lines','author'])
    csvobj.writeheader()
    for quote in quotes:
        csvobj.writerow(quote)