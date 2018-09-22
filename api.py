#!/usr/bin/env python
import os
from urllib import request
import tweepy
import json
from urllib import request
import PIL
from PIL import Image

consumer_key = "JgOX6hGUqwuinsCNhWqH3kfyx"
consumer_secret = "T2N12J3UfcFCTsOWWbN7H6CUW3rT4kJLfPUty1gi5QT4gUbj22"
access_key = "1038805938021572610-Haksy0HfFqfaL1qf3y0eb888sZsJ55"
access_secret = "2pwPVAfk2GOc8QmjLb7lrDPm9bwnPIfe2of0RwR0lKJLF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# for tweet in tweepy.Cursor(api.search,q='Zelda').items(5):
#     print('Tweet by: @' + tweet.user.screen_name)

# search_results = api.search(q='Zelda',count=1)

#for tweet in search_results:
	#print(tweet)
urllist=[]
media_files = set()
for status in tweepy.Cursor(api.home_timeline,screen_name='tomb').items(60):
    if 'media' in status.entities:
    	for image in status.entities['media']:
        	#print(image['media_url'])
        	urllist.append(image['media_url'])



#	jpg_link = 'http://img.my.csdn.net/uploads/201212/25/1356422284_1112.jpg'  #图片链接
#print (urllist)
#	request.urlretrieve(jpg_link, '/home/ece-student/Desktop/1.jpg')

for m in range(len(urllist)):
	print(urllist[m])
	jpg_link = urllist[m]  #图片链接
	request.urlretrieve(jpg_link, '/home/ece-student/Desktop/api/'+'%s.jpg' %m)
	imgfile=str(m)+'.jpg'
	downpath = os.path.join('/home/ece-student/Desktop/api/',imgfile)
	img= Image.open(downpath)
	img = img.resize((1500,1000), Image.ANTIALIAS)
	savepath = os.path.join('/home/ece-student/Desktop/jpg/',imgfile)
	img.save(savepath)