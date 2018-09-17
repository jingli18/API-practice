from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    ttFont = ImageFont.truetype('/home/ece-student/Desktop/Important.ttf', size=96)
    fillcolor = "#3498DB"
    width, height = img.size
    draw.text((width-1090, 100), 'He is a brother-in-brother', fill=fillcolor, font=ttFont)
    img.save('result.jpg','jpeg')

    return 0
if __name__ == '__main__':
    image = Image.open('/home/ece-student/Desktop/guo.jpg')
    add_num(image)
    image.show()

