from youtube_search import YoutubeSearch

results = YoutubeSearch('search terms', max_results=10).to_json()

print(results)
 

results = YoutubeSearch('search terms', max_results=10).to_dict()

print(type(results))
 
import pandas as pd


df = pd.DataFrame(results)

df.to_csv("ABC.csv")
