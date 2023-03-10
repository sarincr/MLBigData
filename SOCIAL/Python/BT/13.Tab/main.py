
import pandas as pd
import requests
from bs4 import BeautifulSoup



url='https://en.wikipedia.org/wiki/Economy_of_India' 
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

k=0
for data in soup.find_all('table', {"class":"wikitable"}):
    print (data.text)
    df = pd.read_html(str(data))
    df = pd.concat(df)
    print(df)
    df.to_csv( "Abc.csv", index=False)
