from bs4 import BeautifulSoup
import requests
import texttable as tt
URL = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
page = requests.get(URL)
# print(page.text) --> html content only
soup = BeautifulSoup(page.text,'html.parser')
data = []
data_interator = iter(soup.findAll('td'))
#print(table)
while True:
    try:
        country = next(data_interator).text
        confirmed = next(data_interator).text
        deaths = next(data_interator).next
        continent = next(data_interator).next
        data.append((country,int(confirmed.replace(',','')),int(deaths.replace(',','')),continent))
    except StopIteration:
        break
data.sort(key=lambda row: row[1],reverse=True)
#print(data)

table = tt.Texttable()
table.add_rows([(None,None,None,None)] + data)
table.set_cols_align(('c','c','c','c'))
table.header(('Country','Confirmed Cases','Deaths','Continent'))
print(table.draw())



