import instaloader
bot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(bot.context, 'python_scripts')
print( profile)



# Instagram Handle and Profile ID
print("Username:", profile.username)
print("User ID", profile.userid)
# Number of Followers and Followees
print("# of followers:", profile.followers)
print("# of followees", profile.followees)  
