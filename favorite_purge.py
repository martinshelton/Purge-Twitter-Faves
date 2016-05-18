#!/usr/bin/env python
import sys, os, time
import tweepy

# Use tweepy ('pip install tweepy' https://github.com/tweepy/tweepy)
# Go to http://dev.twitter.com, create an application to generate keys. Enter your keys below.
keys = dict(
consumer_key='your consumer key here',
consumer_secret='your consumer secret here',
access_token='your access token here', 
access_token_secret='enter token secret here'
)

user = "@your_username"

auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)

def purge():
    tweets = api.favorites(user)
    for f in tweets:
        api.destroy_favorite(f.id)
        time.sleep(6) # wait 6 seconds between requests to avoid rate limit.

if __name__ == "__main__":
    while 1:
        purge()