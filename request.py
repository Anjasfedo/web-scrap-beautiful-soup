from bs4 import BeautifulSoup

import requests

URL = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=golang&txtLocation="

html_text = requests.get(URL).text

soup = BeautifulSoup(html_text, "lxml")

jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")
    
    skills = job.find("span", class_="srp-skills").text.replace(" ", "")
    
    # print(company_name.text.replace(" ", ""))

    # print(skills.text.replace(" ", ""))
    
    print(f'''
          Company Name: {company_name}
          Required Skills: {skills}
          ''')

