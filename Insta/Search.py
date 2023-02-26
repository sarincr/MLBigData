import instaloader
 
bot = instaloader.Instaloader()
 
search_results = instaloader.TopSearchResults(bot.context, 'music')
 
for username in search_results.get_profiles():
    print(username)
 
for hashtag in search_results.get_hashtags():
    print(hashtag)
