import requests, re
from bs4 import BeautifulSoup

r = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/phones").content
soup = BeautifulSoup(r, 'html.parser')
tags = soup.findAll("div", {"class":re.compile('(thumbnail)')})
for h4 in tags:
    a = h4.findAll("h4",{"class":"pull-right price"})
    print(a[0].string)