import io
import os
from urllib import request
import tweepy
import json
from urllib import request
import PIL
from PIL import Image


#twiter download images

#get keys from txt
keypath = os.getcwd()
keypath = keypath + '/keys.txt'
info = open(keypath)
ky = info.readlines()
keyinfo = []
for line in ky:
	keyinfo.append(line.replace('\n', ''))
#write keys to tweepy
consumer_key = keyinfo[0]
consumer_secret = keyinfo[1]
access_key = keyinfo[2]
access_secret = keyinfo[3]

# consumer_key = "JgOX6hGUqwuinsCNhWqH3kfyx"
# consumer_secret = "T2N12J3UfcFCTsOWWbN7H6CUW3rT4kJLfPUty1gi5QT4gUbj22"
# access_key = "1038805938021572610-Haksy0HfFqfaL1qf3y0eb888sZsJ55"
# access_secret = "2pwPVAfk2GOc8QmjLb7lrDPm9bwnPIfe2of0RwR0lKJLF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
print (api)

#get img
imgpath = os.getcwd()
imgpath1= imgpath + "/img/" 
imgpath2= imgpath + "/img2/"
urllist=[]
media_files = set()
for status in tweepy.Cursor(api.home_timeline,screen_name='tomb').items(60):
	if 'media' in status.entities:
		for image in status.entities['media']:
			urllist.append(image['media_url'])

for m in range(len(urllist)):
	print(urllist[m])
	jpg_link = urllist[m]  
	request.urlretrieve(jpg_link, imgpath1+'%s.jpg' %m)
	imgfile=str(m)+'.jpg'
	downpath = os.path.join(imgpath1,imgfile)
	img= Image.open(downpath)
	img = img.resize((1500,1000), Image.ANTIALIAS)
	savepath = os.path.join(imgpath2,imgfile)
	img.save(savepath)
	print(savepath)
