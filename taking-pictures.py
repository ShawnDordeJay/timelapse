from time import sleep
import time
from datetime import date as Date
from datetime import datetime as DateTime
from datetime import timedelta as TimeDelta
import picamera
import glob
import os
import shutil
import sys

WAIT_TIME = 8
#today = Date.today()
now = DateTime.now()
hour = now.strftime('%H')
path = '/home/pi/pictures'

with picamera.PiCamera() as camera:
	camera.resolution = (1280,720)
	camera.annotate_text = DateTime.now().strftime('%d-%m-%Y %H:%M')
	#taking pictures
	for filename in camera.capture_continuous(path+'/img{timestamp:%H-%M-%S-%f}.jpg'):
		sys.stdout.write('took picture\n')
		sys.stdout.flush()
		sleep(WAIT_TIME)
		camera.annotate_text = DateTime.now().strftime('%d-%m-%Y %H:%M')
		#if new day, generate video
		#if today < Date.today():
		"""
		if now.hour < DateTime.now().hour :
			#get files and sort by creation date
			files = glob.glob(path+'/*.jpg')
			files.sort(key=os.path.getmtime)

			#os.system("ffmpeg -r 25 -pattern_type glob -i '/home/pi/pictures/img*.jpg' -s hd1080 -vcodec libx264 timelapse.mp4")
			#os.rename('timelapse.mp4', time.strftime('%d%m%Y')+'.mp4')
			#delete all pictures
			#for file in files:
			#	os.remove(file)
			#set new today

			sys.stdout.write('trying create new folder\n')
                	sys.stdout.flush()
			newfolder = path+'/'+hour
			try:
                                os.mkdir(newfolder)
                        except OSError:
                                print("Creation of the directory %s failed" % newfolder)
                        else:
                                print("Successfully created the directory %s " % newfolder)
                        sys.stdout.write('move files to folder\n')
                        sys.stdout.flush()

			for f in files:
				shutil.move(f, newfolder)

			now = DateTime.now()
			hour = now.strftime('%H')
                        sys.stdout.write('new hour = ' + hour+'\n')
                        sys.stdout.flush()
		"""


