'''
Using tweepy, create a script that programmatically tweets to your twitter account.

Create a JSON file that includes a number of tweets you want to post.
Your script should read from that JSON file, select some text and tweet it
whenever you run the script.

BONUS: Look into CRON jobs to automate your tweets to go out at scheduled times.
       E.g.: "Don't start without me, I'm nearly there!" every weekday at 9:14... ;P

'''


import tweepy
import json
import time

from Documents import twitter_token

file = "Documents/tweets.JSON"


with open(file, "r") as fin:
    tweets = json.load(fin)

auth = tweepy.OAuthHandler(twitter_token.API_key, twitter_token.API_secret_key)
auth.set_access_token(twitter_token.API_token, twitter_token.API_secret_token)
api = tweepy.API(auth)

for tweet in tweets["My_Tweets"]:
    text = tweet["Tweet"]
    api.update_status(text)
    time.sleep(5)


