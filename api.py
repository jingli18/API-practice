#!/usr/bin/env python

import tweepy
import json

consumer_key = "JgOX6hGUqwuinsCNhWqH3kfyx"
consumer_secret = "T2N12J3UfcFCTsOWWbN7H6CUW3rT4kJLfPUty1gi5QT4gUbj22"
access_key = "1038805938021572610-Haksy0HfFqfaL1qf3y0eb888sZsJ55"
access_secret = "2pwPVAfk2GOc8QmjLb7lrDPm9bwnPIfe2of0RwR0lKJLF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search,q='Zelda').items(5):
    print('Tweet by: @' + tweet.user.screen_name)

search_results = api.search(q='Zelda',count=1)

for tweet in search_results:
	print(tweet)

#media_files = set()
#for status in tweepy.Cursor(api.home_timeline,screen_name='Zelda').items(250):
#    if 'media' in status.entities:
#        for image in status.entities['media']:
#            print(image['media_url'])