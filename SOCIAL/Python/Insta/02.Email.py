import instaloader
import re
bot = instaloader.Instaloader()
profile = instaloader.Profile.from_username(bot.context, "wealth")
print("Username: ", profile.username)
print("Bio: ", profile.biography)
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
print("Emails extracted from the bio:")
print(emails)
