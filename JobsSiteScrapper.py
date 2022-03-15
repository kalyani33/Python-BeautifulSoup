import requests
from bs4 import BeautifulSoup
import time
import lxml
print("Put some skill that you are not familiar with")
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}...")

def find_jobs():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    htmldata = requests.get(url).text
    soup = BeautifulSoup(htmldata, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').text
        if 'few' in published_date:
            role = job.header.h2.a.text
            company = job.header.h3.text
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            moreinfo = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f"posts/{index}.txt",'w') as f:
                    f.write(f"Job Role: {role.strip()}\n")
                    f.write(f"CompanyName: {company.strip()}\n")
                    f.write(f"Skills: {skills.strip()}\n")
                    f.write(f"More Info: {moreinfo.strip()}\n")
                    f.write('')
                print(f"file {index}.txt saved...")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"waiting {time_wait} minutes...")
        # this will run for every 10 minutes duartion
        time.sleep(time_wait * 60)



