
import pandas as pd
import requests
from bs4 import BeautifulSoup



page = requests.get('https://en.wikipedia.org/wiki/Economy_of_India').text
soup = BeautifulSoup(page, 'html.parser')
table = soup.find('table', class_="wikitable")

df = pd.read_html(str(table))
df = pd.concat(df)
print(df)
df.to_csv("elections.csv", index=False)



