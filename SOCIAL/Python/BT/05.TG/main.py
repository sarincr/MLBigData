
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Economy_of_India"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib') 

tag = soup.title
print(tag.string)
print(soup.title.string)

