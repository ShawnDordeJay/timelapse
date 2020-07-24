from time import sleep
import time
from datetime import date as Date
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta
import picamera
import glob
import os
import shutil

WAIT_TIME = 5
#today = Date.today()
now = DateTime.now()
minute = now.strftime('%M')
path = '/home/pi/pictures'

with picamera.PiCamera() as camera:
	camera.resolution = (1280,720)
	#taking pictures
	for filename in camera.capture_continuous(path+'/img{timestamp:%H-%M-%S-%f}.jpg'):
		sleep(WAIT_TIME)

		#if new day, generate video
		#if today < Date.today():
		if now.minute < DateTime.now().minute :
			#get files and sort by creation date
			files = glob.glob(path+'/*.jpg')
			files.sort(key=os.path.getmtime)

			#os.system("ffmpeg -r 25 -pattern_type glob -i '/home/pi/pictures/img*.jpg' -s hd1080 -vcodec libx264 timelapse.mp4")
			#os.rename('timelapse.mp4', time.strftime('%d%m%Y')+'.mp4')
			#delete all pictures
			#for file in files:
			#	os.remove(file)
			#set new today
			newfolder = path+'/'+minute
			try:
                                os.mkdir(newfolder)
                        except OSError:
                                print("Creation of the directory %s failed" % newfolder)
                        else:
                                print ("Successfully created the directory %s " % newfolder)

			for f in files:
				shutil.move(f, newfolder)

			now = DateTime.now()
			minute = now.strftime('%M')




