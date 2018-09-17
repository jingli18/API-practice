import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    '/home/ece-student/Desktop/1.jpg')

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

from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    ttFont = ImageFont.truetype('/home/ece-student/Desktop/Important.ttf', size=60)
    fillcolor = "#3498DB"
    width, height = img.size
    i = 0
#    for label in labels:
    	draw.text((width-1100, 100+i), "He is a brother-in-brother", fill=fillcolor, font=ttFont)
    	img.save('result.jpg','jpeg')
    	i=i+80

    return 0
if __name__ == '__main__':
    image = Image.open('/home/ece-student/Desktop/guo.jpg')
    add_num(image)
    image.show()

