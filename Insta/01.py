import instaloader
import pandas as pd
bot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(bot.context, 'leomessi')
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers Count: ", profile.followers)
print("Following Count: ", profile.followees)
print("Bio: ", profile.biography)
print("External URL: ", profile.external_url)
