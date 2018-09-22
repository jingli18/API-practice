import io
import os
from subprocess import Popen, PIPE
from PIL import Image, ImageDraw, ImageFont
from google.cloud import vision
from google.cloud.vision import types


tagpaths = os.getcwd()
tagpath = tagpaths + '/tagimg/'
imgpath = os.getcwd()
imgpath2= imgpath + "/img2/"

# Instantiates a client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=tagpaths + '/PNG vision-003b735f10a8.json'
client = vision.ImageAnnotatorClient()
for n in range(16):
	imgfile=str(n)+'.jpg'
	pathimg=os.path.join(imgpath2,imgfile)
# The name of the image file to annotate
	file_name = os.path.join(
 	os.path.dirname(__file__),
   	pathimg)

# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()
		image = types.Image(content=content)

# Performs label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations

	print('Labels:')
	for label in labels:
		print(label.description)



	image = Image.open(pathimg)
	draw = ImageDraw.Draw(image)
	ttFont = ImageFont.truetype(tagpaths+'/Important.ttf', size=55)
	fillcolor = "#3498DB"
	width, height= image.size
	i = 0
	for label in labels:
		draw.text((width-1490, height-990+i), label.description, fill=fillcolor, font=ttFont)
		
		i=i+60
	savepath = os.path.join(tagpath,imgfile)
	image.save(savepath)
		
		
	
	
		
	n=n+1

os.chdir(tagpath)
os.popen('ffmpeg -loop 1 -i %d.jpg -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" -r 0.5 -t 60 vi.mp4','r',1)
#os.popen('ffmpeg -r 1 -i %d.jpg -vcodec libx264 -y -an video.mp4')
print ("Done")
# print(p.read())

