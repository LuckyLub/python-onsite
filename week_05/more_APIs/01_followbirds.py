'''
Using the tweepy package, build a script that separates twitter handles
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''

import tweepy

from Documents import twitter_token

def classifier(nr_of_followers):
    if nr_of_followers < 10:
        return "Loser"
    elif nr_of_followers >= 10 and nr_of_followers < 50:
        return "Beginner"
    elif nr_of_followers >= 50 and nr_of_followers < 100:
        return "Cool"
    elif nr_of_followers >= 100 and nr_of_followers >= 1000:
        return "Awesome"
    else:
        return "Super star"


auth = tweepy.OAuthHandler(twitter_token.API_key, twitter_token.API_secret_key)
auth.set_access_token(twitter_token.API_token, twitter_token.API_secret_token)

api = tweepy.API(auth, wait_on_rate_limit=True)

result = {}
person = "dan_wegmann"
followers = api.followers(person)
result[person] = classifier(followers.__len__())

for person in followers:
    result[person.screen_name] = classifier(api.followers(person).__len__())

print(result)

