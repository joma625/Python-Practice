# Use 'BeautifulSoup and 'requests packages to print a list of all the article titles on the New York Times homepage

import requests as re
from bs4 import BeautifulSoup as bs

connect = re.get('https://www.nytimes.com/')
source = connect.text

soup = bs(source, 'lxml')

print(soup.h1)


