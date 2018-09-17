from subprocess import Popen, PIPE
import os

p = os.popen('ffmpeg -r 1 -i /home/ece-student/Desktop/api/%d.jpg -vcodec libx264 -y -an video.mp4 -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2"')
#p= os.popen('ffmpeg -f image2 -i  /home/ece-student/Desktop/api%d.jpg -vcodec libx264 -r 25 -b 200k  test.mp4  ')
print(p.read())
#process = Popen([])