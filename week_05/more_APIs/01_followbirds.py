'''
Using the tweepy package, build a script that separates twitter handles
into different groups according to the number of their followers.

The classes can be whatever you like (e.g. I used ASCII art birds ;)

CHALLENGE: Also fetch the number of their friends and display the ratio
between followers and friends in an interesting way.

'''

import tweepy

from Documents import twitter_token

auth = tweepy.OAuthHandler(twitter_token.API_key, twitter_token.API_secret_key)
auth.set_access_token(twitter_token.API_token, twitter_token.API_secret_token)

api = tweepy.API(auth)

api.update_status("Learning how to use the API!")

