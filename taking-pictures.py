from time import sleep
import time
from datetime import datetime as DateTime
import picamera
import os
import sys

WAIT_TIME = 8
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

