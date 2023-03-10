import requests

URL = "https://docs.python.org/3/tutorial/index.html"
page = requests.get(URL)

print(page.text)
