from time import sleep
import time
from datetime import date as Date
from datetime import timedelta as TimeDelta
import picamera
import glob
import os
#import ffmpeg

WAIT_TIME = 5
today = Date.today()

with picamera.PiCamera() as camera:
	camera.resolution = (1280,720)
	#j = 0
	#x = 0
	#taking pictures
	for filename in camera.capture_continuous('/home/pi/pictures/img{timestamp:%H-%M-%S-%f}.jpg'):
		sleep(WAIT_TIME)
		#j += 1
		#if new day, generate video
		if today < Date.today():
		#if j == 5 :
			#get files and sort by creation date
			files = glob.glob('/home/pi/pictures/*.jpg')
			files.sort(key=os.path.getmtime)
			#ffmpeg.input('/home/pi/pictures/*.jpg', pattern_type='glob', framerate=25)
			#ffmpeg.output('timelapse.mp4')
			#ffmpeg.run()

			os.system("ffmpeg -r 24 -pattern_type glob -i '/home/pi/pictures/img*.jpg' -s hd1080 -vcodec libx264 timelapse.mp4")
			os.rename('timelapse.mp4', time.strftime('%d%m%Y')+'.mp4')
			#delete all pictures
			for file in files:
				os.remove(file)
			#set new today
			today = Date.today()

			#j = 0
			#x += 1

