
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Economy_of_India"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib') 
 
for url in soup.find_all('a'):
    print(url.get('href'))
