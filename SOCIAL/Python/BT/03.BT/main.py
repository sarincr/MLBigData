
import requests
from bs4 import BeautifulSoup

URL = "https://docs.python.org/3/tutorial/index.html"

r = requests.get(URL)

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.title)
