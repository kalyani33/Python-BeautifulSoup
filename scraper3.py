import csv

import requests
from bs4 import BeautifulSoup


url = 'https://coreyms.com/'
htmldata = requests.get(url).text
soup = BeautifulSoup(htmldata,'html.parser')
#print(soup.prettify())
numOfPages = soup.find('div',class_='archive-pagination pagination').ul
numOfPages = numOfPages.find_all('li')
numOfPages = numOfPages[-2].a.text
#print(numOfPages)
headings = []
paras = []
links = []
# for page in range(1,int(numOfPages)+1):
#     url = 'https://coreyms.com/page/'+str(page)
#     htmldata = requests.get(url).text
#     soup = BeautifulSoup(htmldata, 'html.parser')
#     for heading in soup.find_all(class_='entry-title-link'):
#         heading = heading.text
#         headings.append(heading)
#     for para  in soup.find_all('div',class_='entry-content'):
#         para = para.p.text
#         paras.append(para)
#     for link in soup.find_all('iframe',class_='youtube-player'):
#         link = link['src']
#         links.append(link)
articles =[]
for page in range(1,int(numOfPages)+1):
    url = 'https://coreyms.com/page/'+str(page)
    htmldata = requests.get(url).text
    soup = BeautifulSoup(htmldata, 'html.parser')
    for heading,para,link in zip(soup.find_all(class_='entry-title-link'),soup.find_all('div',class_='entry-content'),soup.find_all('iframe',class_='youtube-player')):
        article = {}
        article['heading'] = heading.text
        article['para'] = para.p.text
        article['link'] = link['src']
        articles.append(article)

filename = "corey_blog.csv"
with open(filename,'w',newline='')as file:
    csvobj = csv.DictWriter(file,['heading','para','link'])
    csvobj.writeheader()
    csvobj.writerows(articles)
#print(articles)

#print(headings)


