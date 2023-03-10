
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Economy_of_India"

res = requests.get(URL)
soup = BeautifulSoup(res.text)


x = soup.select("img+ .nowrap , tr:nth-child(10) li:nth-child(1)")
print(x)
