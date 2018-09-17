from urllib import request

urls=['http://pbs.twimg.com/media/DnP0kNcVAAAHhHC.jpg','http://pbs.twimg.com/media/DnPk-p7U0AAuozP.jpg']

for i in urls:
	print(i)

	jpg_link = i  #图片链接
	request.urlretrieve(jpg_link, '/home/ece-student/Desktop/api/'+'%s.jpg' %i)