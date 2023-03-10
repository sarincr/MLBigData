
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/search/title?genres=drama&groups=top_250&sort=user_rating,desc"
res = requests.get(url)
soup = BeautifulSoup(res.text)


movies = soup.select(".lister-item-header a")

#print(movies)

movies_titles = [title.text for title in movies]
#movies_links = ["http://imdb.com"+title["href"] for title in movies]
print(movies_titles)
#print(movies_links)
