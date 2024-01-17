from bs4 import BeautifulSoup

import requests

URL = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=golang&txtLocation="

html_text = requests.get(URL).text

soup = BeautifulSoup(html_text, "lxml")

job = soup.find("li", class_="clearfix job-bx wht-shd-bx")

print(job)