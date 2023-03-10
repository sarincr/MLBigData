from bs4 import BeautifulSoup

with open("HTML File.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
print(soup.title)
print(soup.h1)
