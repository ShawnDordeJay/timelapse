from time import sleep
from datetime import datetime as DateTime
import glob
import os
from shutil import copyfile
import shutil

WAIT_TIME = 5
path = '/home/pi/pictures'
now = DateTime.now()
minute = now.strftime('%M')

while 1 :
	newfolder = path+'/'+minute

	if os.path.isdir(newfolder) :

		os.system('ffmpeg -r 24 -pattern_type glob -i \'' + newfolder + '/img*.jpg\' -s hd1080 -vcodec libx264 timelapse.mp4')
		os.rename('timelapse.mp4', minute+'.mp4')
		shutil.move(minute+'.mp4', newfolder)

		files = glob.glob(newfolder+'/*.jpg')
                print('remove files')
		for file in files :
			os.remove(file)


	now = DateTime.now()
	minute = now.strftime('%M')
	print('sleeeeeeep')
	sleep(WAIT_TIME)

